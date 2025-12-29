#!/bin/bash
set -e
python3 -m venv jellyfish-env
source jellyfish-env/bin/activate
pip install -r requirements.txt
chmod +x jellyfish.py
sudo ln -sf $(pwd)/jellyfish.py /usr/bin/jellyfish
cp banner.txt ~/.jellyfish_banner
echo "[+] Jellyfish ready. Run: jellyfish <url>"
