#!/usr/bin/env python3
"""Pipeline and opportunity tracking for Lead Connector."""

import json
import sys
from typing import Optional
from lc_client import LeadConnectorClient


def list_pipelines(client: LeadConnectorClient, location_id: str):
    """List all pipelines for a location."""
    return client.get("/opportunities/pipelines", params={"locationId": location_id})


def list_opportunities(client: LeadConnectorClient, location_id: str, pipeline_id: Optional[str] = None,
                       stage_id: Optional[str] = None, status: str = "open", limit: int = 100):
    """List opportunities with optional filters."""
    params = {"locationId": location_id, "status": status, "limit": limit}
    if pipeline_id:
        params["pipelineId"] = pipeline_id
    if stage_id:
        params["stageId"] = stage_id
    return client.get("/opportunities", params=params)


def get_opportunity(client: LeadConnectorClient, opportunity_id: str):
    """Get a single opportunity by ID."""
    return client.get(f"/opportunities/{opportunity_id}")


def create_opportunity(client: LeadConnectorClient, location_id: str, pipeline_id: str, stage_id: str,
                       title: str, contact_id: str, monetary_value: int = 0, status: str = "open"):
    """Create a new opportunity."""
    payload = {
        "locationId": location_id,
        "pipelineId": pipeline_id,
        "stageId": stage_id,
        "status": status,
        "title": title,
        "contactId": contact_id,
        "monetaryValue": monetary_value,
    }
    return client.post("/opportunities", json=payload)


def update_opportunity(client: LeadConnectorClient, opportunity_id: str, **fields):
    """Update opportunity fields (e.g., stageId, status, monetaryValue)."""
    return client.put(f"/opportunities/{opportunity_id}", json=fields)


def move_stage(client: LeadConnectorClient, opportunity_id: str, new_stage_id: str):
    """Move opportunity to a different stage."""
    return update_opportunity(client, opportunity_id, stageId=new_stage_id)


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  pipeline_tracker.py pipelines <location_id>")
        print("  pipeline_tracker.py opportunities <location_id> [pipeline_id] [stage_id]")
        print("  pipeline_tracker.py get <opportunity_id>")
        print("  pipeline_tracker.py create <location_id> <pipeline_id> <stage_id> <title> <contact_id> [monetary_value]")
        print("  pipeline_tracker.py move <opportunity_id> <new_stage_id>")
        sys.exit(1)

    client = LeadConnectorClient()
    action = sys.argv[1]

    if action == "pipelines":
        result = list_pipelines(client, sys.argv[2])
    elif action == "opportunities":
        result = list_opportunities(
            client, sys.argv[2],
            sys.argv[3] if len(sys.argv) > 3 else None,
            sys.argv[4] if len(sys.argv) > 4 else None
        )
    elif action == "get":
        result = get_opportunity(client, sys.argv[2])
    elif action == "create":
        value = int(sys.argv[7]) if len(sys.argv) > 7 else 0
        result = create_opportunity(client, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], value)
    elif action == "move":
        result = move_stage(client, sys.argv[2], sys.argv[3])
    else:
        print(f"Unknown action: {action}")
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
