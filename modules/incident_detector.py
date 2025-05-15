import re
import os
import hashlib
from datetime import datetime

PROCESSED_INCIDENTS_FILE = "processed_incidents.txt"

if os.path.exists(PROCESSED_INCIDENTS_FILE):
    with open(PROCESSED_INCIDENTS_FILE, "r") as f:
        processed_incidents = set(f.read().splitlines())
else:
    processed_incidents = set()

def hash_incident(incident):
    return hashlib.sha256(incident.encode()).hexdigest()

def save_processed_incident(hash_id):
    with open(PROCESSED_INCIDENTS_FILE, "a") as f:
        f.write(f"{hash_id}\n")

def log_to_file(message, logfile="incidents.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

def detect_incidents(logs):
    incidents = []

    for line in logs:
        # Detekcja nieudanych logowań SSH
        if re.search(r"Failed password for", line):
            incident = f"Nieudane logowanie SSH: {line}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)

        # Detekcja użycia sudo
        if re.search(r"sudo: .* : TTY=", line):
            incident = f"Użycie sudo: {line}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)

        # Detekcja logowania na root
        if re.search(r"session opened for user root", line):
            incident = f"Logowanie na konto root: {line}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)

        # Restart usług systemowych
        if re.search(r"systemd.*(Stopped|Started|Restarted) (.+?)\.service", line):
            service = re.search(r"(Stopped|Started|Restarted) (.+?)\.service", line).group(2)
            incident = f"Restart lub zmiana stanu usługi systemowej: {service}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)

        # Dodanie nowego użytkownika
        if re.search(r"useradd\[\d+\]: new user:", line):
            incident = f"Dodano nowego użytkownika: {line}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)

        # Dodanie użytkownika do sudo
        if re.search(r"usermod.*-aG sudo", line):
            incident = f"Użytkownik dodany do grupy sudo: {line}"
            hash_id = hash_incident(incident)
            if hash_id not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(hash_id)
                log_to_file(incident)
                save_processed_incident(hash_id)
    return incidents