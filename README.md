# DigitalOcean Marketplace 1-Click Apps

This repository contains Packer templates and scripts to build DigitalOcean Marketplace 1-Click Apps for:

- **[Pangolin](https://github.com/fosrl/pangolin)** - A self-hosted tunneled mesh reverse proxy with access control
- **[PMM3](https://github.com/percona/pmm)** - Percona Monitoring and Management 3, an open source database monitoring solution

## TL;DR - Quick Build

Packer will create a DigitalOcean droplet, install the application and its dependencies, then save the system as a reusable image (snapshot) for the Marketplace.

### For Pangolin:
```bash
# Install Packer plugin
packer init plugins.pkr.hcl

# Set API token
export DIGITALOCEAN_API_TOKEN=your_digitalocean_token

# Validate and build
packer validate pangolin-24-04/template.json
packer build pangolin-24-04/template.json
```

### For PMM3:
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
marketplace-templates/
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
├── pangolin-24-04/
│   ├── scripts/
│   │   ├── 010-pangolin.sh
│   │   └── 020-firewall.sh
│   └── template.json
└── pmm3-24-04/
    ├── scripts/
    │   ├── 010-pmm3.sh
    │   └── 020-firewall.sh
    └── template.json
```

## Building the Image

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/marketplace-templates.git
   cd marketplace-templates
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
   # For Pangolin
   packer validate pangolin-24-04/template.json
   
   # For PMM3
   packer validate pmm3-24-04/template.json
   ```

6. Build the image:
   ```bash
   # For Pangolin
   packer build pangolin-24-04/template.json
   
   # For PMM3
   packer build pmm3-24-04/template.json
   ```

7. The build will output a snapshot ID. Note this ID for submission to the Marketplace.

## Submitting to the DigitalOcean Marketplace

1. Log in to the [DigitalOcean Vendor Portal](https://cloud.digitalocean.com/vendorportal).

2. Submit your app with the following details:

   **For Pangolin:**
   - **Name**: Pangolin
   - **Version**: 1.2.0
   - **Software Included**:
     - Pangolin 1.2.0
     - Docker CE (latest)
   - **Image ID**: [The snapshot ID from the Packer build]

   **For PMM3:**
   - **Name**: Percona Monitoring and Management 3
   - **Version**: 3.0.0
   - **Software Included**:
     - PMM3 3.0.0
     - Docker CE (latest)
   - **Image ID**: [The snapshot ID from the Packer build]

3. Complete the rest of the submission form with relevant details about the application.

## For End Users

### Pangolin Users
Once the Pangolin image is approved and available in the Marketplace, users can deploy it by:

1. Selecting "Pangolin" from the DigitalOcean Marketplace.
2. Creating a Droplet based on the image.
3. Pointing a domain to the Droplet's IP address.
4. SSH'ing into the Droplet, where they'll be guided through initial setup.

### PMM3 Users
Once the PMM3 image is approved and available in the Marketplace, users can deploy it by:

1. Selecting "Percona Monitoring and Management 3" from the DigitalOcean Marketplace.
2. Creating a Droplet based on the image (minimum 2GB RAM recommended).
3. SSH'ing into the Droplet, where they'll see the welcome screen with access information.
4. Accessing the PMM3 web interface at `https://YOUR_DROPLET_IP:443`
5. Logging in with default credentials (admin/admin) and changing the password immediately.
6. Adding their databases for monitoring.

## Troubleshooting

If you encounter issues during the build:

1. Add the `-debug` flag to prompt for confirmation at each build step:
   ```bash
   # For Pangolin
   packer build -debug pangolin-24-04/template.json
   
   # For PMM3
   packer build -debug pmm3-24-04/template.json
   ```

2. Use the `-on-error=ask` flag to debug failed builds:
   ```bash
   # For Pangolin
   packer build -on-error=ask pangolin-24-04/template.json
   
   # For PMM3
   packer build -on-error=ask pmm3-24-04/template.json
   ```

3. Enable verbose logging:
   ```bash
   # For Pangolin
   PACKER_LOG=1 packer build pangolin-24-04/template.json
   
   # For PMM3
   PACKER_LOG=1 packer build pmm3-24-04/template.json
   ```

## License

Pangolin is dual licensed under the AGPL-3 and the Fossorial Commercial license.
