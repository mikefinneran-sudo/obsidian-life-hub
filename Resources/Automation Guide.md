# Automation Guide

## Overview

Obsidian Life Hub includes powerful automation that runs in the background to keep your vault organized and up-to-date.

---

## Quick Commands

After running `install.sh`, you'll have these commands available in your terminal:

### Core Commands

```bash
obs-daily       # Create today's daily note
obs-metrics     # Update revenue metrics
obs-open        # Open Dashboard in Obsidian
obs-vault       # Navigate to vault directory
```

### Sync Commands (Optional)

```bash
obs-sync-email  # Sync Gmail → Obsidian
obs-sync-cal    # Sync Google Calendar → Today's note
obs-sync-all    # Sync both email & calendar
```

---

## Automatic Daily Notes

**What it does:** Creates a new daily note every morning at 7 AM automatically.

**How it works:**
- Uses macOS LaunchAgent (set up by `install.sh`)
- Runs `.scripts/create_daily_note.sh`
- Creates note from template in `Daily/YYYY-MM-DD.md`

**Manual creation:**
```bash
obs-daily
```

**To change the time:**
1. Edit `~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist`
2. Change the `Hour` value (24-hour format)
3. Run: `launchctl unload ~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist`
4. Run: `launchctl load ~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist`

---

## Metrics Tracking

**What it does:** Updates revenue metrics in Dashboard and Revenue Tracker.

**Usage:**
```bash
obs-metrics
```

**Interactive prompts:**
- Current MRR
- Number of customers
- Optional notes

**What it updates:**
- Dashboard.md metrics section
- Resources/Revenue Tracker.md table
- Calculates daily average automatically
- Shows progress toward $3,000/month goal

---

## Email & Calendar Sync (Optional)

### Setup Required

1. Enable Gmail API and Google Calendar API
2. Download OAuth credentials
3. Place credentials in vault root as `credentials.json`

**Detailed setup:** See `Resources/Sync Setup Guide.md`

### Gmail Sync

**What it syncs:**
- Last 50 emails from inbox
- Creates note for each important email
- Saved in `Email/` folder

**Usage:**
```bash
obs-sync-email
```

### Calendar Sync

**What it syncs:**
- Today's calendar events
- Adds to today's daily note
- Updates automatically

**Usage:**
```bash
obs-sync-cal
```

---

## Customization

### Change Daily Note Template

Edit `Templates/Daily Note Template.md` to customize what appears in each daily note.

### Add Custom Scripts

Place new scripts in `.scripts/` folder and add aliases to your `.zshrc`:

```bash
alias obs-custom="python3 /path/to/vault/.scripts/custom_script.py"
```

### Disable Auto Daily Notes

```bash
launchctl unload ~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist
```

### Change Vault Location

If you move the vault, re-run `install.sh` from the new location to update paths.

---

## Troubleshooting

### Commands not found

**Solution:** Restart your terminal or run:
```bash
source ~/.zshrc
```

### Permission errors

**Solution:**
```bash
chmod +x .scripts/*.sh
chmod +x .scripts/*.py
```

### Auto daily notes not working

**Check if LaunchAgent is loaded:**
```bash
launchctl list | grep obsidian
```

**Reload it:**
```bash
launchctl unload ~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist
launchctl load ~/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist
```

---

## Windows/Linux Users

### Daily Notes
Create a scheduled task (Windows) or cron job (Linux) to run:
```bash
/path/to/vault/.scripts/create_daily_note.sh
```

### Commands
Add aliases to `.bashrc` instead of `.zshrc`

---

**Need Help?** See `Resources/Quick Start Guide.md` or check the README.
