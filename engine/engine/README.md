# Jellyfish Security Inspector

Audit‑grade **defensive web security engine** for authorized testing.
Built for **accuracy, stability, and low false‑positives**.

## Highlights
- Adaptive safe fuzzing (context‑aware)
- Differential analysis (baseline vs injected)
- Evidence correlation with confidence scoring
- Clean, aesthetic CLI output

## Features
- Parameter discovery (URL + GET forms)
- XSS reflected detection (HTML/ATTR/JS)
- SQL injection indication (error‑based + behavioral)
- Cookie security analysis
- Security headers & TLS posture
- Risk levels: LOW / MEDIUM / HIGH / CRITICAL

## Install
```bash
git clone https://github.com/yubbiXploit86/jellyfish.git
cd jellyfish
chmod +x install.sh
./install.sh

Usage
jellyfish https://example.com/page.php?id=1
