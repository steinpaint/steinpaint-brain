# OpenClaw User Guide

A simple guide for managing OpenClaw without needing to be technical.

---

## 1. Set Up Recurring Tasks (Cron Jobs)

Want Claw to do something automatically every day, week, or hour? Use cron jobs.

### How to Create One

1. **Open your terminal** (Terminal app on Mac)
2. **Type this command** to create a new job:

```bash
openclaw cron add "remind me every Monday at 9am to check the pipeline"
```

Or for something more specific:

```bash
openclaw cron add "sync leads to Google Sheets every 6 hours"
```

3. **Claw will ask you to confirm** the schedule — just say yes or adjust it

### Common Examples

| What You Want | What to Type |
|--------------|--------------|
| Daily morning reminder | `"remind me every day at 8am to check emails"` |
| Weekly report | `"send me a lead summary every Friday at 5pm"` |
| Every few hours | `"check for new leads every 4 hours"` |
| Specific time | `"remind me on May 15th at 2pm about the meeting"` |

### See Your Jobs

```bash
openclaw cron list
```

### Remove a Job

```bash
openclaw cron remove <job-id>
```

(Use `openclaw cron list` to find the job ID)

---

## 2. Start OpenClaw Gateway

The gateway is what keeps Claw running and listening for messages.

### Check If It's Running

```bash
openclaw gateway status
```

### Start It

```bash
openclaw gateway start
```

### Stop It

```bash
openclaw gateway stop
```

### Restart It

```bash
openclaw gateway restart
```

**Note:** OpenClaw is already set to start automatically when your Mac boots. You only need these commands if you want to manually control it.

---

## 3. Change the AI Model

Want Claw to use a different AI model? Maybe something faster, cheaper, or smarter?

### See Available Models

```bash
openclaw models list
```

### Switch Models

```bash
openclaw models use <model-name>
```

For example:

```bash
openclaw models use gpt-4o
```

Or:

```bash
openclaw models use claude-sonnet-4
```

### Set Different Models for Different Tasks

You can use a lightweight model for quick tasks and a powerful one for complex work:

```bash
openclaw models use gpt-4o --for reasoning
openclaw models use gpt-4o-mini --for quick
```

### Check Current Model

```bash
openclaw status
```

This shows what model is currently active.

---

## 4. Quick Reference

| Task | Command |
|------|---------|
| See all commands | `openclaw help` |
| Check status | `openclaw status` |
| View logs | `openclaw logs` |
| Update OpenClaw | `openclaw update` |
| Configure settings | `openclaw configure` |

---

## Need Help?

Just ask Claw: "How do I..." and he'll guide you through it.
