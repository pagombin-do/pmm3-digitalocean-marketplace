#!/usr/bin/env python

"""
This script adds DigitalOcean DBaaS instances to a Percona Monitoring and Management 
(PMM) host running on the local server. Currently only MySQL DBaaS instances are supported.

Updated for PMM v3 API:
- Updated list services endpoint to use /v1/inventory/services (GET)
- Updated to use PMM v3 two-step process: create node first, then service
- Node creation uses /v1/inventory/nodes with 'remote' node type
- Service creation uses /v1/inventory/services with node_id reference
- Updated payload format to use service type as top-level property (PMM v3 format)
- Added Python 2/3 compatibility
- Enhanced error handling for PMM v3 response format
"""

from __future__ import print_function
import os
import sys
import argparse
import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from random import choice
from string import ascii_letters, digits

# Python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass


class PmmServer:
    def __init__(self, baseURL="https://127.0.0.1:443", serverAdminPassword=None):
        self.baseURL = baseURL
        self.password = serverAdminPassword
    
    def listServices(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        # Updated endpoint for PMM v3
        endpoint = self.baseURL + "/v1/inventory/services"
        try:
            r = requests.get(endpoint, verify=False, auth=('admin', self.password))
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if r.status_code == 401:
                print("Invalid PMM admin password.")
            else:
                jsonResponse = r.json()
                print(jsonResponse.get('message', 'HTTP Error occurred'))
            sys.exit(1) 
        except requests.exceptions.RequestException as e:
            print('Could not connect to PMM instance at {}'.format(self.baseURL))
            sys.exit(1)
    
        return r.json()
    
    def addNode(self, mysqlInstance):
        """
        Add a node for the MySQL instance using PMM v3 unified nodes API
        """
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        
        node_body = {
            "remote": {
                "node_name": mysqlInstance.name,
                "address": mysqlInstance.address,
                "region": mysqlInstance.region
            }
        }
        
        endpoint = self.baseURL + "/v1/inventory/nodes"
        try:
            r = requests.post(endpoint, json=node_body, verify=False, auth=('admin', self.password))
            r.raise_for_status()
            response = r.json()
            # Return the node_id from the response
            if 'remote' in response:
                return response['remote']['node_id']
            else:
                print("Unexpected response format when adding node")
                return None
        except requests.exceptions.HTTPError:
            jsonResponse = r.json()
            if r.status_code == 409:
                # Node already exists, try to find it
                print("Node already exists, attempting to find existing node...")
                return self.findExistingNode(mysqlInstance.name)
            else:
                print("Error adding node: {}".format(jsonResponse.get('message', 'Unknown error')))
                return None
        except Exception as err:
            print("Error adding node: {}".format(err))
            return None
    
    def findExistingNode(self, node_name):
        """
        Find an existing node by name
        """
        try:
            endpoint = self.baseURL + "/v1/inventory/nodes"
            r = requests.get(endpoint, verify=False, auth=('admin', self.password))
            r.raise_for_status()
            nodes = r.json()
            
            # Look for the node in different node types
            for node_type in ['generic', 'container', 'remote']:
                if node_type in nodes:
                    for node in nodes[node_type]:
                        if node.get('node_name') == node_name:
                            return node.get('node_id')
            return None
        except Exception as err:
            print("Error finding existing node: {}".format(err))
            return None

    def addMySQL(self, mysqlInstance):
        """
        Given a dict representing a DBaaS MySQL instance, add it to PMM using PMM v3 API
        """
        print("Adding instance {} to PMM...".format(mysqlInstance.name))
    
        mysqlInstance.createMonitoringUser()
        
        # First, create the node
        node_id = self.addNode(mysqlInstance)
        if not node_id:
            print("Failed to add or find node for instance {}".format(mysqlInstance.name))
            return
        
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        # Use PMM v3 inventory API format for services
        body = {
            "mysql": {
                "service_name": mysqlInstance.name,
                "node_id": node_id,
                "address": mysqlInstance.address,
                "port": mysqlInstance.port,
                "environment": mysqlInstance.region,
                "custom_labels": {
                    "source": "digitalocean",
                    "region": mysqlInstance.region
                }
            }
        }
        
        # Use the inventory services endpoint in PMM v3
        addURL = self.baseURL + "/v1/inventory/services"
        try:
            r = requests.post(addURL, json=body, verify=False, auth=('admin', self.password))
            r.raise_for_status()
            print("Successfully added {} to PMM".format(mysqlInstance.name))
        except requests.exceptions.HTTPError:
            jsonResponse = r.json()
            if r.status_code == 409:
                # Service already exists
                print("Service '{}' already exists: {}".format(mysqlInstance.name, jsonResponse.get('message', 'Conflict')))
            else:
                print("Error adding service '{}': {}".format(mysqlInstance.name, jsonResponse.get('message', 'Unknown error')))
        except Exception as err:
            print("Error adding service '{}': {}".format(mysqlInstance.name, err))
    
        return

class DbaasInstance:

    def __init__(self, instanceAttributes, pmmServer):
        self.name = instanceAttributes['name']
        self.region = instanceAttributes['region']
        self.address = instanceAttributes['connection']['host']
        self.port = instanceAttributes['private_connection']['port']
        self.admin_username = instanceAttributes['private_connection']['user']
        self.admin_password = instanceAttributes['private_connection']['password']
        self.engine = instanceAttributes['engine']
        self.monitored = self.instanceMonitored(pmmServer)

    
    def generatePassword(self):
        password = ''.join([choice(ascii_letters + digits)
                    for n in range(32)])
        return password
    
    def createMonitoringUser(self):
        self.monitoring_username = 'pmm'
        self.monitoring_password = self.generatePassword()
        return
    
    def instanceMonitored(self, pmmServer):
        """
        Return boolean based on if an instance is monitored according to PMM API
        """
        services = pmmServer.listServices()
        try:
            # Updated for PMM v3 response structure
            mysqlServices = services.get('mysql', [])
        except (KeyError, AttributeError):
            mysqlServices = []
        if (self.address, self.port) in [ (i.get('address'), i.get('port')) for i in mysqlServices]:
            return True
        else:
            return False


def getAPIToken():
    token = os.environ.get('DIGITALOCEAN_API_TOKEN')
    if not token:
        token = input("Enter your DigitalOcean API token: ")
    return token

def getPMMAdminPassword():
    password = os.environ.get('PMM_ADMIN_PASSWORD')
    if not password:
        password = input("Enter the password for the PMM 'admin' user: ")
    return password

def getDBInstances(token):
    """
    Fetch all DBaaS instances from DigitalOcean API
    """
    auth_header = {"Authorization": "Bearer {}".format(token)}
    try:
        r = requests.get('https://api.digitalocean.com/v2/databases', headers=auth_header)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 401:
            print("Invalid DigitalOcean API token.")
        else:
            jsonResponse = r.json()
            print(jsonResponse['error'])
        sys.exit(1) 
    except Exception as err:
        print(err)  
        sys.exit(1) 
    return r.json()['databases']

def promptForDBSelection(instances):
    """
    Display list of eligible DBaaS instances and prompt user to enter selection. 
    Returns list if selected instances.
    """
    selectedInstances = []
    print('Eligible DBaaS instances found:') 
    for instance in instances:
        print('- {}'.format(instance.name), end = '')
        if instance.monitored:
            print(' (monitored)')
        else:
            print('')
    try:
        user_input = input('Enter comma-separated list of database names to monitor [all]: ')
    except (KeyboardInterrupt, EOFError):
        print('')
        sys.exit(0)
    if len(user_input) == 0:
        selectedInstanceNames = ['all']
    else:
        selectedInstanceNames = [ s.strip() for s in user_input.split(',') ]
    if 'all' in selectedInstanceNames:
        validInstances = instances
    else:
        validInstances = [ i for i in instances if i.name in selectedInstanceNames ]
    return validInstances

def getPublicIPv4():
    """
    Return the public IPv4 address of localhost
    """
    try:
        r = requests.get("http://169.254.169.254/metadata/v1/interfaces/public/0/ipv4/address")
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        jsonResponse = r.json()
        print(jsonResponse['error'])
    except Exception as err:
        print(err)
    return r.content

def printBanner():
    print(
"""
# This script adds DigitalOcean DBaaS instances to a Percona Monitoring and Management 
# (PMM) host running on the local server. Currently only MySQL DBaaS instances are supported.
# 
# Before attempting to add DBaaS instances, make sure you have logged in to the Percona 
# Monitoring and Management GUI and set an admin password using this URL:
# 
# http://{}/
#
# Ensure that PMM is able to connect to your DBaaS instances by adding the PMM server
# to each database's Trusted Sources list here: https://cloud.digitalocean.com/databases.
# 
# This script will prompt for your PMM password and DigitalOcean API token which can 
# be generated at https://cloud.digitalocean.com/account/api/tokens (read-only permissions
# are sufficient). You can set these using environment variables:
# 
# export DIGITALOCEAN_API_TOKEN=<_your_API_token_>
# export PMM_ADMIN_PASSWORD=<_your_PMM_password_>
""".format(getPublicIPv4())
)


def main(arguments):

    printBanner()
    
    digitalocean_api_token = getAPIToken()
    pmm_admin_password = getPMMAdminPassword()
    pmm = PmmServer(serverAdminPassword=pmm_admin_password)
    
    instanceProperties = getDBInstances(digitalocean_api_token)
    eligibleInstances = [ DbaasInstance(i, pmm) for i in instanceProperties if i['engine'] in ['mysql']]
    selectedInstances = promptForDBSelection(eligibleInstances)
    for instance in selectedInstances:
        if instance.monitored:
            print('Instance "{}" is already monitored by PMM.'.format(instance.name))
            continue
        if instance.engine == 'mysql':
            pmm.addMySQL(instance)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))