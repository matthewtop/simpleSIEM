import re

processed_incidents = set()

def detect_incidents(logs):
    incidents = []

    for line in logs:
        # Detekcja nieudanych logowań SSH
        if re.search(r"Failed password for", line):
            incident = f"Nieudane logowanie SSH: {line}"
            if incident not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(incident)

        # Detekcja użycia sudo
        if re.search(r"sudo: .* : TTY=", line):
            incident = f"Użycie sudo: {line}"
            if incident not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(incident)

        # Detekcja logowania na root
        if re.search(r"session opened for user root", line):
            incident = f"Logowanie na konto root: {line}"
            if incident not in processed_incidents:
                incidents.append(incident)
                processed_incidents.add(incident)

    return incidents