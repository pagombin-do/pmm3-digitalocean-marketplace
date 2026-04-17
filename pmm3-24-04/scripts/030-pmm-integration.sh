#!/bin/sh
# ---------------------------------------------------------------------------
# PMM Integration Installer — Packer build variant
#
# Installs the PMM Integration web app during 1-Click image creation.
# App source files ship inside this repo at pmm3-24-04/pmm-integration/
# and are uploaded to /tmp/pmm-integration/ on the build Droplet by Packer
# before this script runs.
# ---------------------------------------------------------------------------

set -eu

SRC_DIR="/tmp/pmm-integration"
INSTALL_DIR="/opt/pmm-integration"
SERVICE_NAME="pmm-integration"
PORT="${PORT:-8443}"
CERT_DIR="$INSTALL_DIR/certs"
VENV_DIR="$INSTALL_DIR/venv"
UNIT_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

info()  { printf '\033[1;34m[INFO]\033[0m  %s\n' "$*"; }
ok()    { printf '\033[1;32m[OK]\033[0m    %s\n' "$*"; }
fail()  { printf '\033[1;31m[ERROR]\033[0m %s\n' "$*"; exit 1; }

info "PMM Integration Installer"
echo "=============================================="

if [ "$(id -u)" -ne 0 ]; then
    fail "This installer must be run as root."
fi

if [ ! -d "$SRC_DIR" ]; then
    fail "Expected app files at $SRC_DIR (uploaded by Packer) but directory is missing."
fi

# System dependencies
info "Installing system dependencies..."
apt-get update -qq
apt-get install -y -qq python3 python3-pip python3-venv openssl > /dev/null 2>&1
ok "System dependencies installed."

# Firewall — open the HTTPS port
if command -v ufw >/dev/null 2>&1; then
    if ufw status 2>/dev/null | grep -q "Status: active"; then
        info "Opening port ${PORT}/tcp in ufw..."
        ufw allow "${PORT}/tcp" >/dev/null
        ok "Firewall rule added: allow ${PORT}/tcp."
    fi
fi

# Copy app files into place
info "Copying application files to $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"
cp -r "$SRC_DIR"/. "$INSTALL_DIR"/
ok "Application files in place."

cd "$INSTALL_DIR"

# Python virtual environment
info "Creating Python virtual environment..."
python3 -m venv "$VENV_DIR"
. "$VENV_DIR/bin/activate"

info "Installing Python dependencies..."
pip install --upgrade pip -q
pip install -r "$INSTALL_DIR/requirements.txt" -q
ok "Python dependencies installed."

# TLS certificate — self-signed, loopback SANs only
# (Customer's Droplet IP is unknown at build time, so we don't bake it in.)
info "Generating self-signed TLS certificate..."
mkdir -p "$CERT_DIR"
openssl req -x509 -newkey rsa:2048 -nodes \
    -keyout "$CERT_DIR/key.pem" \
    -out "$CERT_DIR/cert.pem" \
    -days 3650 \
    -subj "/CN=pmm-integration" \
    -addext "subjectAltName=IP:127.0.0.1,DNS:localhost" \
    2>/dev/null
chmod 600 "$CERT_DIR/key.pem"
ok "Self-signed TLS certificate generated (valid 10 years)."

# systemd service
info "Creating systemd unit file..."
cat > "$UNIT_FILE" <<EOF
[Unit]
Description=PMM Integration Web Application
After=network.target

[Service]
Type=simple
WorkingDirectory=$INSTALL_DIR
ExecStart=$INSTALL_DIR/venv/bin/python3 $INSTALL_DIR/app.py
Environment=PORT=$PORT
Environment=LISTEN_HOST=0.0.0.0
Environment=TLS_CERT_DIR=$CERT_DIR
Environment=PMM_BASE_URL=https://127.0.0.1:443
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable "$SERVICE_NAME" --quiet
ok "Service enabled; will start on boot."

# Clean up the staged files so they aren't captured in the image snapshot
rm -rf "$SRC_DIR"

echo ""
echo "=============================================="
ok "PMM Integration installed."
echo "  Service will start on boot and listen on port $PORT."
echo "  Customers access it at: https://<droplet_ip>:${PORT}/"
echo "=============================================="
