import json
from datetime import datetime

def classify_issue(user_input: str):
    """Classify issue type"""
    keywords = {
        "bug": ["error", "fail", "not working", "issue"],
        "access": ["access", "permission", "login"],
        "infra": ["server", "down", "cpu", "memory"],
        "request": ["need", "request", "create", "setup"]
    }

    for category, words in keywords.items():
        if any(word in user_input.lower() for word in words):
            return category

    return "general"


def create_ticket(data: dict):
    """Create structured ticket"""
    ticket = {
        "id": f"TICKET-{int(datetime.now().timestamp())}",
        "title": data.get("title"),
        "description": data.get("description"),
        "priority": data.get("priority", "Medium"),
        "type": data.get("type"),
        "created_at": str(datetime.now())
    }

    return ticket
