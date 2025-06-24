Title: Add a Service

URL Source: https://percona-pmm.readme.io/reference/addservice

Markdown Content:
Add a Service

===============

[Jump to Content](https://percona-pmm.readme.io/reference/addservice#content)

[![Image 1: Percona Monitoring and Management](https://files.readme.io/1f1bf6e-small-Percona_Horizontal_logo_fullcolor_whitetext.png)](https://percona-pmm.readme.io/reference)

[API Reference](https://percona-pmm.readme.io/reference)

* * *

[Log In](https://percona-pmm.readme.io/login?redirect_uri=/reference/addservice)[![Image 2: Percona Monitoring and Management](https://files.readme.io/1f1bf6e-small-Percona_Horizontal_logo_fullcolor_whitetext.png)](https://percona-pmm.readme.io/reference)

API Reference

[Log In](https://percona-pmm.readme.io/login?redirect_uri=/reference/addservice)

PMM v3

[API Reference](https://percona-pmm.readme.io/reference)Add a Service

Search

CTRL-K

All

Reference

###### Start typing to search…

JUMP TO CTRL-/

WELCOME
-------

*   [Introduction](https://percona-pmm.readme.io/reference/introduction)
*   [Authentication](https://percona-pmm.readme.io/reference/authentication)
*   [Monitoring](https://percona-pmm.readme.io/reference/monitoring)

Release Notes
-------------

*   [PMM v3 API release notes](https://percona-pmm.readme.io/reference/release-notes-3-0-0)

PMM API
-------

*   [ServerService](https://percona-pmm.readme.io/reference/leaderhealthcheck)
    *   [Check Leadership get](https://percona-pmm.readme.io/reference/leaderhealthcheck)
    *   [Logs get](https://percona-pmm.readme.io/reference/logs)
    *   [Check server readiness get](https://percona-pmm.readme.io/reference/readiness)
    *   [Get settings get](https://percona-pmm.readme.io/reference/getsettings)
    *   [Change settings put](https://percona-pmm.readme.io/reference/changesettings)
    *   [Check updates get](https://percona-pmm.readme.io/reference/checkupdates)
    *   [Get the changelog get](https://percona-pmm.readme.io/reference/listchangelogs)
    *   [Update status post](https://percona-pmm.readme.io/reference/updatestatus)
    *   [Start update post](https://percona-pmm.readme.io/reference/startupdate)
    *   [Version get](https://percona-pmm.readme.io/reference/version)

*   [UserService](https://percona-pmm.readme.io/reference/listusers)
    *   [List all users get](https://percona-pmm.readme.io/reference/listusers)
    *   [Get user details get](https://percona-pmm.readme.io/reference/getuser)
    *   [Update a user put](https://percona-pmm.readme.io/reference/updateuser)

*   [AgentsService](https://percona-pmm.readme.io/reference/listagents)
    *   [List Agents get](https://percona-pmm.readme.io/reference/listagents)
    *   [Add an Agent post](https://percona-pmm.readme.io/reference/addagent)
    *   [Get Agent get](https://percona-pmm.readme.io/reference/getagent)
    *   [Change Agent Attributes put](https://percona-pmm.readme.io/reference/changeagent)
    *   [Remove an Agent from Inventory delete](https://percona-pmm.readme.io/reference/removeagent)
    *   [Get Agent logs get](https://percona-pmm.readme.io/reference/getagentlogs)

*   [NodesService](https://percona-pmm.readme.io/reference/listnodes)
    *   [List Nodes get](https://percona-pmm.readme.io/reference/listnodes)
    *   [Add a Node post](https://percona-pmm.readme.io/reference/addnode)
    *   [Get a Node get](https://percona-pmm.readme.io/reference/getnode)
    *   [Remove a Node delete](https://percona-pmm.readme.io/reference/removenode)

*   [ServicesService](https://percona-pmm.readme.io/reference/listservices)
    *   [List Services get](https://percona-pmm.readme.io/reference/listservices)
    *   [Add a Service post](https://percona-pmm.readme.io/reference/addservice)
    *   [Get a Service get](https://percona-pmm.readme.io/reference/getservice)
    *   [Change service put](https://percona-pmm.readme.io/reference/changeservice)
    *   [Remove Service delete](https://percona-pmm.readme.io/reference/removeservice)
    *   [List Active Service Types post](https://percona-pmm.readme.io/reference/listactiveservicetypes)

*   [ManagementService](https://percona-pmm.readme.io/reference/listagentsmixin3)
    *   [List Agents get](https://percona-pmm.readme.io/reference/listagentsmixin3)
    *   [List Agent Versions get](https://percona-pmm.readme.io/reference/listagentversions)
    *   [Add an Annotation post](https://percona-pmm.readme.io/reference/addannotation)
    *   [List Nodes get](https://percona-pmm.readme.io/reference/listnodesmixin3)
    *   [Register a Node post](https://percona-pmm.readme.io/reference/registernode)
    *   [Get Node get](https://percona-pmm.readme.io/reference/getnodemixin3)
    *   [Unregister a Node delete](https://percona-pmm.readme.io/reference/unregisternode)
    *   [List Services get](https://percona-pmm.readme.io/reference/listservicesmixin3)
    *   [Add a Service post](https://percona-pmm.readme.io/reference/addservicemixin3)
    *   [Add Azure Database post](https://percona-pmm.readme.io/reference/addazuredatabase)
    *   [Remove a Service delete](https://percona-pmm.readme.io/reference/removeservicemixin3)
    *   [Discover Azure Database post](https://percona-pmm.readme.io/reference/discoverazuredatabase)
    *   [Discover RDS post](https://percona-pmm.readme.io/reference/discoverrds)

*   [ActionsService](https://percona-pmm.readme.io/reference/getaction)
    *   [Get Action get](https://percona-pmm.readme.io/reference/getaction)
    *   [Cancel an Action post](https://percona-pmm.readme.io/reference/cancelaction)
    *   [Start 'PT Summary' Action post](https://percona-pmm.readme.io/reference/startptsummaryaction)
    *   [Start a Service Action post](https://percona-pmm.readme.io/reference/startserviceaction)

*   [AlertingService](https://percona-pmm.readme.io/reference/createrule)
    *   [CreateRule creates alerting rule from the given template.post](https://percona-pmm.readme.io/reference/createrule)
    *   [ListTemplates returns a list of all collected alert rule templates.get](https://percona-pmm.readme.io/reference/listtemplates)
    *   [CreateTemplate creates a new template.post](https://percona-pmm.readme.io/reference/createtemplate)
    *   [UpdateTemplate updates existing template, previously created via API.put](https://percona-pmm.readme.io/reference/updatetemplate)
    *   [DeleteTemplate deletes existing, previously created via API.delete](https://percona-pmm.readme.io/reference/deletetemplate)

*   [AdvisorService](https://percona-pmm.readme.io/reference/listadvisors)
    *   [List Advisors get](https://percona-pmm.readme.io/reference/listadvisors)
    *   [List Advisor Checks get](https://percona-pmm.readme.io/reference/listadvisorchecks)
    *   [Get Failed Advisor Checks get](https://percona-pmm.readme.io/reference/getfailedchecks)
    *   [Change Advisor Checks post](https://percona-pmm.readme.io/reference/changeadvisorchecks)
    *   [Start Advisor Checks post](https://percona-pmm.readme.io/reference/startadvisorchecks)
    *   [List Failed Services get](https://percona-pmm.readme.io/reference/listfailedservices)

*   [BackupService](https://percona-pmm.readme.io/reference/listartifacts)
    *   [List artifacts get](https://percona-pmm.readme.io/reference/listartifacts)
    *   [Delete Artifact delete](https://percona-pmm.readme.io/reference/deleteartifact)
    *   [List PITR Timeranges get](https://percona-pmm.readme.io/reference/listpitrtimeranges)
    *   [List Scheduled Backups get](https://percona-pmm.readme.io/reference/listscheduledbackups)
    *   [List Compatible Services get](https://percona-pmm.readme.io/reference/listartifactcompatibleservices)
    *   [Get Logs get](https://percona-pmm.readme.io/reference/getlogs)
    *   [Remove a Scheduled Backup delete](https://percona-pmm.readme.io/reference/removescheduledbackup)
    *   [Change a Scheduled Backup put](https://percona-pmm.readme.io/reference/changescheduledbackup)
    *   [Schedule a Backup post](https://percona-pmm.readme.io/reference/schedulebackup)
    *   [Make a backup post](https://percona-pmm.readme.io/reference/startbackup)

*   [LocationsService](https://percona-pmm.readme.io/reference/listlocations)
    *   [List Locations get](https://percona-pmm.readme.io/reference/listlocations)
    *   [Add a Backup Location post](https://percona-pmm.readme.io/reference/addlocation)
    *   [Change a Backup Location put](https://percona-pmm.readme.io/reference/changelocation)
    *   [Remove a Scheduled Backup delete](https://percona-pmm.readme.io/reference/removelocation)
    *   [Test a Backup Location and Credentials post](https://percona-pmm.readme.io/reference/testlocationconfig)

*   [RestoreService](https://percona-pmm.readme.io/reference/listrestores)
    *   [List Restore History get](https://percona-pmm.readme.io/reference/listrestores)
    *   [Get Logs get](https://percona-pmm.readme.io/reference/getlogsmixin5)
    *   [Restore from a backup post](https://percona-pmm.readme.io/reference/restorebackup)

*   [QANService](https://percona-pmm.readme.io/reference/getfilteredmetricsnames)
    *   [Get Filters post](https://percona-pmm.readme.io/reference/getfilteredmetricsnames)
    *   [Get Metrics Names post](https://percona-pmm.readme.io/reference/getmetricsnames)
    *   [Get Report post](https://percona-pmm.readme.io/reference/getreport)
    *   [Get Query Plan get](https://percona-pmm.readme.io/reference/getqueryplan)
    *   [Check Query Existence post](https://percona-pmm.readme.io/reference/queryexists)
    *   [Get Query Example post](https://percona-pmm.readme.io/reference/getqueryexample)
    *   [Get Schema post](https://percona-pmm.readme.io/reference/schemabyqueryid)
    *   [Get Explain Fingerprint post](https://percona-pmm.readme.io/reference/explainfingerprintbyqueryid)
    *   [Get Histogram post](https://percona-pmm.readme.io/reference/gethistogram)
    *   [Get Labels post](https://percona-pmm.readme.io/reference/getlabels)
    *   [Get Metrics post](https://percona-pmm.readme.io/reference/getmetrics)

*   [PlatformService](https://percona-pmm.readme.io/reference/getcontactinformation)
    *   [Get Contact Information get](https://percona-pmm.readme.io/reference/getcontactinformation)
    *   [Search Organization Entitlements get](https://percona-pmm.readme.io/reference/searchorganizationentitlements)
    *   [Search Organization Tickets get](https://percona-pmm.readme.io/reference/searchorganizationtickets)
    *   [Get Server Info get](https://percona-pmm.readme.io/reference/serverinfo)
    *   [Get User Status get](https://percona-pmm.readme.io/reference/userstatus)
    *   [Connect PMM Server post](https://percona-pmm.readme.io/reference/connect)
    *   [Disconnect PMM Server post](https://percona-pmm.readme.io/reference/disconnect)

INVENTORY API
-------------

*   [Overview](https://percona-pmm.readme.io/reference/pmm-inventory)

PMM SERVER MAINTENANCE
----------------------

*   [Overview](https://percona-pmm.readme.io/reference/pmm-server-configuration)
*   [User account management](https://percona-pmm.readme.io/reference/pmm-server-user-accounts)
    *   [Change the administrator's password](https://percona-pmm.readme.io/reference/change-admin-password)
    *   [Create user accounts](https://percona-pmm.readme.io/reference/create-user-accounts)

*   [Upgrade your PMM Server](https://percona-pmm.readme.io/reference/pmm-server-upgrade)
*   [Troubleshooting](https://percona-pmm.readme.io/reference/pmm-server-logs)
    *   [Logs](https://percona-pmm.readme.io/reference/pmm-server-logs)

ADVISOR API
-----------

*   [Overview](https://percona-pmm.readme.io/reference/pmm-advisors)

BACKUP API
----------

*   [Overview](https://percona-pmm.readme.io/reference/database-backups)

ACCESS CONTROL API
------------------

*   [Overview](https://percona-pmm.readme.io/reference/access-control)

Add a Service
=============

post https://example.com/v1/inventory/services

Adds a Service.

Add a Service

[](https://percona-pmm.readme.io/reference/addservice#add-a-service)
-----------------------------------------------------------------------------------

This section describes how to add a Service of any type to PMM Inventory.

In PMM versions prior to 3.0.0, we featured a separate API call for each Service type. Starting with PMM 3.0.0, we have streamlined the process by offering single API endpoint for all Service types.

Previously, the Service type was defined by the endpoint, i.e. `Services/AddMySQL`. In the new approach, the Service type must be specified as the top-level property of the request payload. As part of the single API endpoint update, we have deprecated individual API endpoints for each Service type.

Here's how to add a Node of type `mysql` using the old and the new API calls:

**Old API call**:

Shell

```shell
curl --insecure -X POST \
     --header 'Authorization: Bearer XXXXX' \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --url https://127.0.0.1/v1/inventory/Services/AddMySQL \
     --data '
{
  "service_name": "mysql-sales-db-prod-1",
  "node_id": "pmm-server",
  "address":  "209.0.25.100",
  "port": 3306,
  "environment": "sales-prod",
  "cluster": "db-sales-prod-1",
  "replication_set": "db-sales-prod-1-rs1",
  "custom_labels": {
    "department":  "sales"
  }
}
'
```

**New API call**:

Shell

```shell
curl --insecure -X POST \
     --header 'Authorization: Bearer XXXXX' \
     --header 'Content-Type: application/json' \
     --url https://127.0.0.1/v1/inventory/services \
     --data '
{
  "mysql": {
    "service_name": "mysql-sales-db-prod-1",
    "node_id": "pmm-server",
    "address":  "209.0.25.100",
    "port": 3306,
    "environment": "sales-prod",
    "cluster": "db-sales-prod-1",
    "replication_set": "db-sales-prod-1-rs1",
    "custom_labels": {
      "department":  "sales"
    }
  }
}
'
```

You can choose from the following Service types:

*   mysql
*   mongodb
*   postgresql
*   proxysql
*   haproxy
*   external

To get the authentication token, check [Authentication](https://percona-pmm.readme.io/reference/authentication).

Body Params

mysql

object

mysql object

mongodb

object

mongodb object

postgresql

object

postgresql object

proxysql

object

proxysql object

haproxy

object

haproxy object

external

object

external object

Responses

200

A successful response.
=============================

Response body

object

mysql

object

MySQLService represents a generic MySQL instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

node_id 

string

Node identifier where this instance runs.

address 

string

Access address (DNS name or IP).

 Address (and port) or socket is required.

port 

int64

Access port.

 Port is required when the address present.

socket 

string

Access unix socket.

 Address (and port) or socket is required.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

version 

string

MySQL version.

mongodb

object

MongoDBService represents a generic MongoDB instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

node_id 

string

Node identifier where this instance runs.

address 

string

Access address (DNS name or IP).

 Address (and port) or socket is required.

port 

int64

Access port.

 Port is required when the address present.

socket 

string

Access unix socket.

 Address (and port) or socket is required.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

version 

string

MongoDB version.

postgresql

object

PostgreSQLService represents a generic PostgreSQL instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

database_name 

string

Database name.

node_id 

string

Node identifier where this instance runs.

address 

string

Access address (DNS name or IP).

 Address (and port) or socket is required.

port 

int64

Access port.

 Port is required when the address present.

socket 

string

Access unix socket.

 Address (and port) or socket is required.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

version 

string

PostgreSQL version.

auto_discovery_limit 

int32

Limit of databases for auto-discovery.

proxysql

object

ProxySQLService represents a generic ProxySQL instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

node_id 

string

Node identifier where this instance runs.

address 

string

Access address (DNS name or IP).

 Address (and port) or socket is required.

port 

int64

Access port.

 Port is required when the address present.

socket 

string

Access unix socket.

 Address (and port) or socket is required.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

version 

string

ProxySQL version.

haproxy

object

HAProxyService represents a generic HAProxy service instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

node_id 

string

Node identifier where this service instance runs.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

external

object

ExternalService represents a generic External service instance.

service_id 

string

Unique randomly generated instance identifier.

service_name 

string

Unique across all Services user-defined name.

node_id 

string

Node identifier where this service instance runs.

environment 

string

Environment name.

cluster 

string

Cluster name.

replication_set 

string

Replication set name.

custom_labels

object

Custom user-assigned labels.

Has additional fields

group 

string

Group name of external service.

default

An unexpected error response.
========================================

Response body

object

code 

int32

message 

string

details

array of objects

details

object

@type 

string

View Additional Properties

Updated 9 months ago

* * *

[List Services](https://percona-pmm.readme.io/reference/listservices)[Get a Service](https://percona-pmm.readme.io/reference/getservice)

Did this page help you?

Yes

No

Language

Shell Go Node Python

Credentials

Basic

base64

Basic

:

cURL Request

Examples

xxxxxxxxxx

1

curl --request POST \

2

 --url https://example.com/v1/inventory/services \

3

 --header 'accept: application/json' \

4

 --header 'content-type: application/json'

Try It!

RESPONSE

Examples

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

200 default

Updated 9 months ago

* * *

[List Services](https://percona-pmm.readme.io/reference/listservices)[Get a Service](https://percona-pmm.readme.io/reference/getservice)

Did this page help you?

Yes

No

1.   WELCOME
2.   [Introduction](https://percona-pmm.readme.io/reference/introduction)
3.   [Authentication](https://percona-pmm.readme.io/reference/authentication)
4.   [Monitoring](https://percona-pmm.readme.io/reference/monitoring)

1.   Release Notes
2.   [PMM v3 API release notes](https://percona-pmm.readme.io/reference/release-notes-3-0-0)

1.   PMM API
2.   [ServerService](https://percona-pmm.readme.io/reference/serverservice)
3.   [Version get](https://percona-pmm.readme.io/reference/version)
4.   [Start update post](https://percona-pmm.readme.io/reference/startupdate)
5.   [Update status post](https://percona-pmm.readme.io/reference/updatestatus)
6.   [Get the changelog get](https://percona-pmm.readme.io/reference/listchangelogs)
7.   [Check updates get](https://percona-pmm.readme.io/reference/checkupdates)
8.   [Change settings put](https://percona-pmm.readme.io/reference/changesettings)
9.   [Get settings get](https://percona-pmm.readme.io/reference/getsettings)
10.   [Check server readiness get](https://percona-pmm.readme.io/reference/readiness)
11.   [Logs get](https://percona-pmm.readme.io/reference/logs)
12.   [Check Leadership get](https://percona-pmm.readme.io/reference/leaderhealthcheck)
13.   [UserService](https://percona-pmm.readme.io/reference/userservice)
14.   [Update a user put](https://percona-pmm.readme.io/reference/updateuser)
15.   [Get user details get](https://percona-pmm.readme.io/reference/getuser)
16.   [List all users get](https://percona-pmm.readme.io/reference/listusers)
17.   [AgentsService](https://percona-pmm.readme.io/reference/agentsservice)
18.   [Get Agent logs get](https://percona-pmm.readme.io/reference/getagentlogs)
19.   [Remove an Agent from Inventory delete](https://percona-pmm.readme.io/reference/removeagent)
20.   [Change Agent Attributes put](https://percona-pmm.readme.io/reference/changeagent)
21.   [Get Agent get](https://percona-pmm.readme.io/reference/getagent)
22.   [Add an Agent post](https://percona-pmm.readme.io/reference/addagent)
23.   [List Agents get](https://percona-pmm.readme.io/reference/listagents)
24.   [NodesService](https://percona-pmm.readme.io/reference/nodesservice)
25.   [Remove a Node delete](https://percona-pmm.readme.io/reference/removenode)
26.   [Get a Node get](https://percona-pmm.readme.io/reference/getnode)
27.   [Add a Node post](https://percona-pmm.readme.io/reference/addnode)
28.   [List Nodes get](https://percona-pmm.readme.io/reference/listnodes)
29.   [ServicesService](https://percona-pmm.readme.io/reference/servicesservice)
30.   [List Active Service Types post](https://percona-pmm.readme.io/reference/listactiveservicetypes)
31.   [Remove Service delete](https://percona-pmm.readme.io/reference/removeservice)
32.   [Change service put](https://percona-pmm.readme.io/reference/changeservice)
33.   [Get a Service get](https://percona-pmm.readme.io/reference/getservice)
34.   [Add a Service post](https://percona-pmm.readme.io/reference/addservice)
35.   [List Services get](https://percona-pmm.readme.io/reference/listservices)
36.   [ManagementService](https://percona-pmm.readme.io/reference/managementservice)
37.   [Discover RDS post](https://percona-pmm.readme.io/reference/discoverrds)
38.   [Discover Azure Database post](https://percona-pmm.readme.io/reference/discoverazuredatabase)
39.   [Remove a Service delete](https://percona-pmm.readme.io/reference/removeservicemixin3)
40.   [Add Azure Database post](https://percona-pmm.readme.io/reference/addazuredatabase)
41.   [Add a Service post](https://percona-pmm.readme.io/reference/addservicemixin3)
42.   [List Services get](https://percona-pmm.readme.io/reference/listservicesmixin3)
43.   [Unregister a Node delete](https://percona-pmm.readme.io/reference/unregisternode)
44.   [Get Node get](https://percona-pmm.readme.io/reference/getnodemixin3)
45.   [Register a Node post](https://percona-pmm.readme.io/reference/registernode)
46.   [List Nodes get](https://percona-pmm.readme.io/reference/listnodesmixin3)
47.   [Add an Annotation post](https://percona-pmm.readme.io/reference/addannotation)
48.   [List Agent Versions get](https://percona-pmm.readme.io/reference/listagentversions)
49.   [List Agents get](https://percona-pmm.readme.io/reference/listagentsmixin3)
50.   [ActionsService](https://percona-pmm.readme.io/reference/actionsservice)
51.   [Start a Service Action post](https://percona-pmm.readme.io/reference/startserviceaction)
52.   [Start 'PT Summary' Action post](https://percona-pmm.readme.io/reference/startptsummaryaction)
53.   [Cancel an Action post](https://percona-pmm.readme.io/reference/cancelaction)
54.   [Get Action get](https://percona-pmm.readme.io/reference/getaction)
55.   [AlertingService](https://percona-pmm.readme.io/reference/alertingservice)
56.   [DeleteTemplate deletes existing, previously created via API.delete](https://percona-pmm.readme.io/reference/deletetemplate)
57.   [UpdateTemplate updates existing template, previously created via API.put](https://percona-pmm.readme.io/reference/updatetemplate)
58.   [CreateTemplate creates a new template.post](https://percona-pmm.readme.io/reference/createtemplate)
59.   [ListTemplates returns a list of all collected alert rule templates.get](https://percona-pmm.readme.io/reference/listtemplates)
60.   [CreateRule creates alerting rule from the given template.post](https://percona-pmm.readme.io/reference/createrule)
61.   [AdvisorService](https://percona-pmm.readme.io/reference/advisorservice)
62.   [List Failed Services get](https://percona-pmm.readme.io/reference/listfailedservices)
63.   [Start Advisor Checks post](https://percona-pmm.readme.io/reference/startadvisorchecks)
64.   [Change Advisor Checks post](https://percona-pmm.readme.io/reference/changeadvisorchecks)
65.   [Get Failed Advisor Checks get](https://percona-pmm.readme.io/reference/getfailedchecks)
66.   [List Advisor Checks get](https://percona-pmm.readme.io/reference/listadvisorchecks)
67.   [List Advisors get](https://percona-pmm.readme.io/reference/listadvisors)
68.   [BackupService](https://percona-pmm.readme.io/reference/backupservice)
69.   [Make a backup post](https://percona-pmm.readme.io/reference/startbackup)
70.   [Schedule a Backup post](https://percona-pmm.readme.io/reference/schedulebackup)
71.   [Change a Scheduled Backup put](https://percona-pmm.readme.io/reference/changescheduledbackup)
72.   [Remove a Scheduled Backup delete](https://percona-pmm.readme.io/reference/removescheduledbackup)
73.   [Get Logs get](https://percona-pmm.readme.io/reference/getlogs)
74.   [List Compatible Services get](https://percona-pmm.readme.io/reference/listartifactcompatibleservices)
75.   [List Scheduled Backups get](https://percona-pmm.readme.io/reference/listscheduledbackups)
76.   [List PITR Timeranges get](https://percona-pmm.readme.io/reference/listpitrtimeranges)
77.   [Delete Artifact delete](https://percona-pmm.readme.io/reference/deleteartifact)
78.   [List artifacts get](https://percona-pmm.readme.io/reference/listartifacts)
79.   [LocationsService](https://percona-pmm.readme.io/reference/locationsservice)
80.   [Test a Backup Location and Credentials post](https://percona-pmm.readme.io/reference/testlocationconfig)
81.   [Remove a Scheduled Backup delete](https://percona-pmm.readme.io/reference/removelocation)
82.   [Change a Backup Location put](https://percona-pmm.readme.io/reference/changelocation)
83.   [Add a Backup Location post](https://percona-pmm.readme.io/reference/addlocation)
84.   [List Locations get](https://percona-pmm.readme.io/reference/listlocations)
85.   [RestoreService](https://percona-pmm.readme.io/reference/restoreservice)
86.   [Restore from a backup post](https://percona-pmm.readme.io/reference/restorebackup)
87.   [Get Logs get](https://percona-pmm.readme.io/reference/getlogsmixin5)
88.   [List Restore History get](https://percona-pmm.readme.io/reference/listrestores)
89.   [QANService](https://percona-pmm.readme.io/reference/qanservice)
90.   [Get Metrics post](https://percona-pmm.readme.io/reference/getmetrics)
91.   [Get Labels post](https://percona-pmm.readme.io/reference/getlabels)
92.   [Get Histogram post](https://percona-pmm.readme.io/reference/gethistogram)
93.   [Get Explain Fingerprint post](https://percona-pmm.readme.io/reference/explainfingerprintbyqueryid)
94.   [Get Schema post](https://percona-pmm.readme.io/reference/schemabyqueryid)
95.   [Get Query Example post](https://percona-pmm.readme.io/reference/getqueryexample)
96.   [Check Query Existence post](https://percona-pmm.readme.io/reference/queryexists)
97.   [Get Query Plan get](https://percona-pmm.readme.io/reference/getqueryplan)
98.   [Get Report post](https://percona-pmm.readme.io/reference/getreport)
99.   [Get Metrics Names post](https://percona-pmm.readme.io/reference/getmetricsnames)
100.   [Get Filters post](https://percona-pmm.readme.io/reference/getfilteredmetricsnames)
101.   [PlatformService](https://percona-pmm.readme.io/reference/platformservice)
102.   [Disconnect PMM Server post](https://percona-pmm.readme.io/reference/disconnect)
103.   [Connect PMM Server post](https://percona-pmm.readme.io/reference/connect)
104.   [Get User Status get](https://percona-pmm.readme.io/reference/userstatus)
105.   [Get Server Info get](https://percona-pmm.readme.io/reference/serverinfo)
106.   [Search Organization Tickets get](https://percona-pmm.readme.io/reference/searchorganizationtickets)
107.   [Search Organization Entitlements get](https://percona-pmm.readme.io/reference/searchorganizationentitlements)
108.   [Get Contact Information get](https://percona-pmm.readme.io/reference/getcontactinformation)

1.   INVENTORY API
2.   [Overview](https://percona-pmm.readme.io/reference/pmm-inventory)

1.   PMM SERVER MAINTENANCE
2.   [Overview](https://percona-pmm.readme.io/reference/pmm-server-configuration)
3.   [User account management](https://percona-pmm.readme.io/reference/pmm-server-user-accounts)
4.   [Create user accounts](https://percona-pmm.readme.io/reference/create-user-accounts)
5.   [Change the administrator's password](https://percona-pmm.readme.io/reference/change-admin-password)
6.   [Upgrade your PMM Server](https://percona-pmm.readme.io/reference/pmm-server-upgrade)
7.   [Troubleshooting](https://percona-pmm.readme.io/reference/pmm-server-troubleshooting)
8.   [Logs](https://percona-pmm.readme.io/reference/pmm-server-logs)

1.   ADVISOR API
2.   [Overview](https://percona-pmm.readme.io/reference/pmm-advisors)

1.   BACKUP API
2.   [Overview](https://percona-pmm.readme.io/reference/database-backups)

1.   ACCESS CONTROL API
2.   [Overview](https://percona-pmm.readme.io/reference/access-control)
