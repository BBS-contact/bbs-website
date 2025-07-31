
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

LOG_FILE = "sos_log.txt"

def log_event(service, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{service.upper()}]\n"
    log_entry += f"Name: {data.get('name')}\n"
    log_entry += f"Location: {data.get('location')}\n"

    if service == 'police':
        log_entry += f"Threat: {data.get('threat')}\n"
    elif service == 'ambulance':
        log_entry += f"Medical Info: {data.get('medical')}\n"
    elif service == 'family':
        log_entry += f"Contact 1: {data.get('family1')}\n"
        log_entry += f"Contact 2: {data.get('family2')}\n"
        log_entry += f"Contact 3: {data.get('family3')}\n"

    log_entry += "-" * 50 + "\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)


def simulate_sms(name, location, message, numbers):
    print("
📲 SIMULATED SMS:")
    for contact in numbers:
        if isinstance(contact, dict):  # новий формат: {'name': '...', 'phone': '...'}
            number = contact.get('phone', 'NoNumber')
            person = contact.get('name', 'Unknown')
            to_field = f"{number} ({person})"
        else:  # старий формат: просто номер
            to_field = contact
        print(f"To: {to_field}")
        print(f"Message: 🚨 SOS
Name: {name}
Location: {location}
{message}")
        print("-" * 40)

