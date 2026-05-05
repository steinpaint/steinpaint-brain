# Lead Connector API Errors & Troubleshooting

## Common HTTP Status Codes

| Code | Meaning | Typical Cause |
|------|---------|---------------|
| 400 | Bad Request | Missing required field, invalid JSON, malformed request |
| 401 | Unauthorized | Invalid or expired API key, missing `Authorization` header |
| 403 | Forbidden | API key lacks permissions for this location/action |
| 404 | Not Found | Resource doesn't exist (wrong ID, deleted contact, etc.) |
| 409 | Conflict | Duplicate email/phone, resource already exists |
| 422 | Unprocessable | Validation error (e.g., invalid stage ID, bad custom field) |
| 429 | Too Many Requests | Rate limit exceeded (100 req/min for private integrations) |
| 500 | Server Error | Lead Connector internal error — retry or contact support |

## Common Errors

### "Invalid API Key" / 401
- Check that `LEAD_CONNECTOR_API_KEY` is set correctly
- Ensure the key is for **Private Integrations** (not OAuth or Agency API)
- Verify the key hasn't expired or been revoked

### "Location ID is required" / 400
- Most endpoints need `locationId` as a query parameter or in the request body
- Get your location ID from the GHL dashboard: Settings > Business Profile > Location ID

### "Contact already exists" / 409
- Lead Connector enforces unique emails per location
- Search for existing contact first, then update instead of create

### "Invalid stageId" / 422
- Stage IDs are unique per pipeline
- List pipelines first to get valid stage IDs
- Pipeline/stage IDs change if pipelines are reconfigured

### Rate Limiting (429)
- Private integrations: 100 requests/minute
- Add delays between bulk operations
- Use batch endpoints where available

## Debugging Tips

1. **Always check the response body** — GHL often returns detailed error messages
2. **Log request/response** — use the Python client's `request()` method for full visibility
3. **Verify IDs** — pipeline IDs, stage IDs, and custom field IDs are not human-readable; fetch them via API
4. **Test with curl first** — isolate whether it's an API issue or a script issue

## Support

- Lead Connector API docs: https://highlevel.stoplight.io/docs/integrations/
- Private integrations setup: GHL dashboard > Settings > Integrations > Private Integrations