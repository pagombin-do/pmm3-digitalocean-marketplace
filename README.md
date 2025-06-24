# PMM3 DigitalOcean Marketplace 1-Click App

This repository contains Packer templates and scripts to build a DigitalOcean Marketplace 1-Click App for:

**[PMM3](https://github.com/percona/pmm)** - Percona Monitoring and Management 3, an open source database monitoring solution

## TL;DR - Quick Build

Packer will create a DigitalOcean droplet, install PMM3 and its dependencies, then save the system as a reusable image (snapshot) for the Marketplace.

```bash
# Install Packer plugin
packer init plugins.pkr.hcl

# Set API token
export DIGITALOCEAN_API_TOKEN=your_digitalocean_token

# Validate and build
packer validate pmm3-24-04/template.json
packer build pmm3-24-04/template.json
```

## Prerequisites

- [Packer](https://www.packer.io/downloads) (v1.7.0 or higher)
- [DigitalOcean Personal Access Token](https://docs.digitalocean.com/reference/api/create-personal-access-token/)
- The [DigitalOcean Packer plugin](https://developer.hashicorp.com/packer/plugins/builders/digitalocean) (for Packer 1.7.0+)

## Directory Structure

```
pmm3-digitalocean-marketplace/
├── common/
│   ├── files/
│   │   └── var/
│   │       └── lib/
│   │           └── digitalocean/
│   └── scripts/
│       ├── 010-docker.sh
│       ├── 018-force-ssh-logout.sh
│       ├── 020-application-tag.sh
│       └── 900-cleanup.sh
└── pmm3-24-04/
    ├── pmm-do.py
    ├── scripts/
    │   ├── 010-pmm3.sh
    │   └── 020-firewall.sh
    └── template.json
```

## Building the Image

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pmm3-digitalocean-marketplace.git
   cd pmm3-digitalocean-marketplace
   ```

2. For Packer 1.7.0+, initialize the DigitalOcean plugin:
   ```bash
   # Create plugins.pkr.hcl file
   cat > plugins.pkr.hcl << EOF
   packer {
     required_plugins {
       digitalocean = {
         version = ">= 1.4.1"
         source  = "github.com/digitalocean/digitalocean"
       }
     }
   }
   EOF

   # Initialize plugins
   packer init plugins.pkr.hcl
   ```

3. Set your DigitalOcean API token as an environment variable:
   ```bash
   export DIGITALOCEAN_API_TOKEN=your_digitalocean_token
   ```

4. Create the necessary directory structure if it doesn't already exist:
   ```bash
   mkdir -p common/files/var/lib/digitalocean
   ```

5. Validate the template:
   ```bash
   packer validate pmm3-24-04/template.json
   ```

6. Build the image:
   ```bash
   packer build pmm3-24-04/template.json
   ```

7. The build will output a snapshot ID. Note this ID for submission to the Marketplace.

## Submitting to the DigitalOcean Marketplace

1. Log in to the [DigitalOcean Vendor Portal](https://cloud.digitalocean.com/vendorportal).

2. Submit your app with the following details:

   - **Name**: Percona Monitoring and Management 3
   - **Version**: 3.0.0
   - **Software Included**:
     - PMM3 3.0.0
     - Docker CE (latest)
     - DigitalOcean Database Integration Script (pmm-do.py)
   - **Image ID**: [The snapshot ID from the Packer build]

3. Complete the rest of the submission form with relevant details about PMM3.

## For End Users

Once the PMM3 image is approved and available in the Marketplace, users can deploy it by:

1. Selecting "Percona Monitoring and Management 3" from the DigitalOcean Marketplace.
2. Creating a Droplet based on the image (minimum 2GB RAM recommended).
3. SSH'ing into the Droplet, where they'll see the welcome screen with access information.
4. Accessing the PMM3 web interface at `https://YOUR_DROPLET_IP:443`
5. Logging in with default credentials (admin/admin) and changing the password immediately.
6. Adding their databases for monitoring.

### DigitalOcean Database Integration

For users with DigitalOcean Managed Databases, the Droplet includes a convenient integration script:

```bash
python3 /root/pmm-do.py
```

This script will:
- Automatically discover MySQL databases in your DigitalOcean account
- Guide you through adding them to PMM3 monitoring
- Configure optimal monitoring settings including Query Analytics
- Set up proper authentication and security settings

## Troubleshooting

If you encounter issues during the build:

1. Add the `-debug` flag to prompt for confirmation at each build step:
   ```bash
   packer build -debug pmm3-24-04/template.json
   ```

2. Use the `-on-error=ask` flag to debug failed builds:
   ```bash
   packer build -on-error=ask pmm3-24-04/template.json
   ```

3. Enable verbose logging:
   ```bash
   PACKER_LOG=1 packer build pmm3-24-04/template.json
   ```

## License

PMM3 (Percona Monitoring and Management) is licensed under the Apache License 2.0.
