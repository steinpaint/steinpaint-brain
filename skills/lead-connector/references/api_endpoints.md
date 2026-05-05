# Lead Connector API Endpoints Reference

## Base URL
`https://services.leadconnectorhq.com`

## Headers Required
- `Authorization: Bearer <API_KEY>`
- `Version: 2021-07-28`
- `Content-Type: application/json` (for POST/PUT)

## Contacts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contacts` | List contacts (requires `locationId`) |
| GET | `/contacts/<id>` | Get contact by ID |
| POST | `/contacts` | Create contact |
| PUT | `/contacts/<id>` | Update contact |
| DELETE | `/contacts/<id>` | Delete contact |
| GET | `/contacts/search` | Search contacts (requires `locationId`, `query`) |

**Query params for list:** `locationId`, `limit` (max 100), `offset`, `query`

## Opportunities / Pipelines

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/opportunities/pipelines` | List pipelines (requires `locationId`) |
| GET | `/opportunities` | List opportunities |
| GET | `/opportunities/<id>` | Get opportunity by ID |
| POST | `/opportunities` | Create opportunity |
| PUT | `/opportunities/<id>` | Update opportunity |
| DELETE | `/opportunities/<id>` | Delete opportunity |

**Query params for opportunities:** `locationId`, `pipelineId`, `stageId`, `status` (open/won/lost/all), `limit`, `offset`

## Campaigns

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/campaigns` | List campaigns (requires `locationId`) |
| GET | `/campaigns/<id>` | Get campaign by ID |

## Appointments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/appointments` | List appointments (requires `locationId`, `startTime`, `endTime`) |
| GET | `/appointments/<id>` | Get appointment by ID |
| POST | `/appointments` | Create appointment |
| PUT | `/appointments/<id>` | Update appointment |
| DELETE | `/appointments/<id>` | Delete appointment |

## Locations

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/locations` | List accessible locations |
| GET | `/locations/<id>` | Get location by ID |

## Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | List users (requires `locationId`) |
| GET | `/users/<id>` | Get user by ID |

## Notes
- Rate limit: 100 requests/minute for private integrations
- Most endpoints require `locationId` as query param or in body
- Monetary values are in cents (e.g., $250.00 = 25000)
- Date/times should be ISO 8601 format (e.g., `2024-06-15T14:00:00.000Z`)