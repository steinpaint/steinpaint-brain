#!/usr/bin/env python3
"""Contact management utilities for Lead Connector."""

import json
import sys
from typing import Optional, List
from lc_client import LeadConnectorClient


def search_contacts(client: LeadConnectorClient, location_id: str, query: str, limit: int = 100):
    """Search contacts by name, email, or phone."""
    params = {"locationId": location_id, "query": query, "limit": limit}
    return client.get("/contacts/search", params=params)


def get_contact(client: LeadConnectorClient, contact_id: str):
    """Get a single contact by ID."""
    return client.get(f"/contacts/{contact_id}")


def create_contact(client: LeadConnectorClient, location_id: str, first_name: str, last_name: str,
                   email: Optional[str] = None, phone: Optional[str] = None, tags: Optional[List[str]] = None,
                   custom_fields: Optional[List[dict]] = None):
    """Create a new contact."""
    payload = {
        "locationId": location_id,
        "firstName": first_name,
        "lastName": last_name,
    }
    if email:
        payload["email"] = email
    if phone:
        payload["phone"] = phone
    if tags:
        payload["tags"] = tags
    if custom_fields:
        payload["customFields"] = custom_fields
    return client.post("/contacts", json=payload)


def update_contact(client: LeadConnectorClient, contact_id: str, **fields):
    """Update contact fields."""
    return client.put(f"/contacts/{contact_id}", json=fields)


def add_tags(client: LeadConnectorClient, contact_id: str, tags: List[str]):
    """Add tags to a contact."""
    return client.put(f"/contacts/{contact_id}", json={"tags": tags})


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  contact_manager.py search <location_id> <query>")
        print("  contact_manager.py get <contact_id>")
        print("  contact_manager.py create <location_id> <first_name> <last_name> [email] [phone]")
        print("  contact_manager.py update <contact_id> <json_fields>")
        sys.exit(1)

    client = LeadConnectorClient()
    action = sys.argv[1]

    if action == "search":
        result = search_contacts(client, sys.argv[2], sys.argv[3])
    elif action == "get":
        result = get_contact(client, sys.argv[2])
    elif action == "create":
        result = create_contact(client, sys.argv[2], sys.argv[3], sys.argv[4],
                                sys.argv[5] if len(sys.argv) > 5 else None,
                                sys.argv[6] if len(sys.argv) > 6 else None)
    elif action == "update":
        result = update_contact(client, sys.argv[2], **json.loads(sys.argv[3]))
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()