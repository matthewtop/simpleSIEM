import subprocess
from datetime import datetime, timedelta

def parse_logs():
    now = datetime.now()
    since_time = (now - timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')  

    try:
        cmd = ["journalctl", "--since", since_time, "--no-pager"]
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        logs = output.decode("utf-8").splitlines()
        return logs
    except Exception as e:
        print(f"[!] Błąd podczas pobierania logów: {e}")
        return []
