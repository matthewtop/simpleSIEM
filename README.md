# 🛡️ SimpleSIEM - Your personal System Log Guardian

A simple, personal (very minimalised and not complicated verion) of your own Security Information and Management System(SIEM written in Python. It analyzes Linux system logs from `journalctl` in near real-time. It detects basic suspicious actions and immediately sends you alert via Telegram. 

## Requirements

* Linux system with `systemd`
* Python 3.7 or higher
* `pip` 
* A Telegram account and Bot created to receive alerts

## Installation & Configuration

1.  **Clone the repository and go to project directory:**
    ```bash
    git clone https://github.com/matthewtop/simpleSIEM.git
    cd simpleSIEM/
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source .venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -p requirements.txt
    ```

4. **Create your own config.yaml file:**
    ```bash
    touch config.yaml
    ```

5. **Using editor of your choice paste it to .yaml file:**
    ```yaml
    # config.yaml
    telegram:
      token: "YOUR_ACTUAL_TELEGRAM_BOT_TOKEN_HERE"
      chat_id: "YOUR_ACTUAL_CHAT_ID_HERE"
    ```

6. **You are ready to run the script with sudo privileges!**
    ```bash
    sudo python3 main.py
    ```
