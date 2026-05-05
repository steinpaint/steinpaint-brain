#!/usr/bin/env python3
"""Lead Connector API client wrapper."""

import os
import sys
import requests
from typing import Optional, Dict, Any

BASE_URL = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"


class LeadConnectorClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("LEAD_CONNECTOR_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set LEAD_CONNECTOR_API_KEY env var or pass to constructor.")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Version": API_VERSION,
            "Content-Type": "application/json",
        })

    def request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{BASE_URL}{endpoint}"
        resp = self.session.request(method, url, **kwargs)
        resp.raise_for_status()
        return resp.json() if resp.text else {}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint: str, json: Optional[Dict] = None) -> Dict[str, Any]:
        return self.request("POST", endpoint, json=json)

    def put(self, endpoint: str, json: Optional[Dict] = None) -> Dict[str, Any]:
        return self.request("PUT", endpoint, json=json)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        return self.request("DELETE", endpoint)


def main():
    """Quick test: list locations or show usage."""
    if len(sys.argv) < 2:
        print("Usage: lc_client.py <endpoint> [method] [json_body]")
        print("Example: lc_client.py /contacts?locationId=xxx")
        sys.exit(1)

    client = LeadConnectorClient()
    endpoint = sys.argv[1]
    method = sys.argv[2].upper() if len(sys.argv) > 2 else "GET"
    body = sys.argv[3] if len(sys.argv) > 3 else None

    kwargs = {}
    if body:
        import json
        kwargs["json"] = json.loads(body)

    result = client.request(method, endpoint, **kwargs)
    import json
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()