---
name: lead-connector
description: "Interact with Lead Connector (GoHighLevel / GHL) CRM via private integrations API. Use when: managing contacts, pipelines, opportunities, campaigns, appointments, or automations in Lead Connector; syncing lead data; creating or updating contacts; moving deals through pipelines; checking campaign status; or any CRM task for Stein Paint's commercial sales workflow."
---

# Lead Connector (GHL) Skill

## Overview

This skill enables interaction with Lead Connector (GoHighLevel) CRM through its private integrations API. Used for managing leads, contacts, pipelines, and campaigns for Stein Paint's commercial sales operations in Miami-Dade and Broward counties.

## Setup

Requires a Lead Connector private integrations API key. Store it in:
- Environment variable: `LEAD_CONNECTOR_API_KEY`
- Or provide directly when prompted

Base URL: `https://services.leadconnectorhq.com`
API Version: `2021-07-28`

## Authentication

All requests require:
```
Authorization: Bearer <API_KEY>
Version: 2021-07-28
```

## Core Capabilities

### 1. Contacts

**List contacts:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/contacts?locationId=<LOCATION_ID>&limit=100"
```

**Get contact by ID:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/contacts/<CONTACT_ID>"
```

**Create contact:**
```bash
curl -X POST \
     -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     -H "Content-Type: application/json" \
     -d '{
       "locationId": "<LOCATION_ID>",
       "firstName": "John",
       "lastName": "Doe",
       "email": "john@hotel.com",
       "phone": "+13055551234",
       "tags": ["hotel", "miami-dade"],
       "customFields": [
         {"id": "<FIELD_ID>", "value": "Hotel Property Manager"}
       ]
     }' \
     "https://services.leadconnectorhq.com/contacts"
```

**Update contact:**
```bash
curl -X PUT \
     -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     -H "Content-Type: application/json" \
     -d '{"tags": ["qualified", "follow-up"]}' \
     "https://services.leadconnectorhq.com/contacts/<CONTACT_ID>"
```

**Search contacts:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/contacts/search?locationId=<LOCATION_ID>&query=<SEARCH_TERM>"
```

### 2. Pipelines & Opportunities

**List pipelines:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/opportunities/pipelines?locationId=<LOCATION_ID>"
```

**List opportunities in pipeline:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/opportunities?pipelineId=<PIPELINE_ID>&locationId=<LOCATION_ID>"
```

**Create opportunity:**
```bash
curl -X POST \
     -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     -H "Content-Type: application/json" \
     -d '{
       "locationId": "<LOCATION_ID>",
       "pipelineId": "<PIPELINE_ID>",
       "stageId": "<STAGE_ID>",
       "status": "open",
       "title": "Hotel Renovation - Downtown Miami",
       "contactId": "<CONTACT_ID>",
       "monetaryValue": 25000,
       "customFields": []
     }' \
     "https://services.leadconnectorhq.com/opportunities"
```

**Update opportunity stage:**
```bash
curl -X PUT \
     -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     -H "Content-Type: application/json" \
     -d '{"stageId": "<NEW_STAGE_ID>"}' \
     "https://services.leadconnectorhq.com/opportunities/<OPPORTUNITY_ID>"
```

### 3. Campaigns

**List campaigns:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/campaigns?locationId=<LOCATION_ID>"
```

**Get campaign by ID:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/campaigns/<CAMPAIGN_ID>"
```

### 4. Appointments

**List appointments:**
```bash
curl -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     "https://services.leadconnectorhq.com/appointments?locationId=<LOCATION_ID>&startTime=2024-01-01T00:00:00.000Z&endTime=2024-12-31T23:59:59.999Z"
```

**Create appointment:**
```bash
curl -X POST \
     -H "Authorization: Bearer $LEAD_CONNECTOR_API_KEY" \
     -H "Version: 2021-07-28" \
     -H "Content-Type: application/json" \
     -d '{
       "locationId": "<LOCATION_ID>",
       "contactId": "<CONTACT_ID>",
       "calendarId": "<CALENDAR_ID>",
       "title": "Site Visit - Hotel Property",
       "startTime": "2024-06-15T14:00:00.000Z",
       "endTime": "2024-06-15T15:00:00.000Z",
       "address": "123 Biscayne Blvd, Miami, FL"
     }' \
     "https://services.leadconnectorhq.com/appointments"
```

## Common Workflows

### New Lead Intake
1. Search for existing contact by email/phone
2. If not found, create contact with tags (e.g., `hotel`, `condo-assoc`, `miami-dade`)
3. Create opportunity in appropriate pipeline
4. Log notes or schedule follow-up appointment

### Pipeline Review
1. List all pipelines for location
2. Get opportunities by pipeline/stage
3. Identify stalled deals (>30 days in stage)
4. Recommend follow-up actions

### Campaign Follow-up
1. List active campaigns
2. Check campaign performance metrics
3. Identify contacts who engaged but didn't convert
4. Create follow-up tasks or opportunities

## Scripts

See `scripts/` directory for reusable Python utilities:
- `lc_client.py` - Authenticated API client wrapper
- `contact_manager.py` - Contact CRUD operations
- `pipeline_tracker.py` - Pipeline and opportunity management

## References

- `references/api_endpoints.md` - Complete endpoint reference
- `references/error_codes.md` - Common errors and troubleshooting

## Notes

- Rate limits: 100 requests/minute for private integrations
- Location ID is required for most operations
- Custom fields must be defined in GHL before use
- Monetary values are in cents (e.g., $250.00 = 25000)