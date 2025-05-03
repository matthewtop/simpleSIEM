import time
from modules.log_parser import parse_logs
from modules.incident_detector import detect_incidents
from modules.notifier import send_alert

CHECK_INTERVAL = 10  

if __name__ == "__main__":
    print("[+] Personal SIEM started...")
    while True:
        logs = parse_logs()
        incidents = detect_incidents(logs)

        for incident in incidents:
            send_alert(incident)

        time.sleep(CHECK_INTERVAL)
