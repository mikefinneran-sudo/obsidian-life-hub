# Customization Guide

## Overview

Obsidian Life Hub is designed to be flexible. Customize it to match your workflow, business, and personal style.

---

## Dashboard Customization

### Edit Your Revenue Goal

Open `Dashboard.md` and change line 17:
```markdown
### Goal: $3,000/month
```

Change to your target (e.g., `$5,000/month`, `$10,000/month`)

### Add Your Projects

Replace the example project with your real projects:

```markdown
### 🚀 In Progress

#### [[Your Project Name]]
**Status:** 🟢 In Progress
**MRR:** $X → Target: $Y
**Next Action:** What you're working on next
```

### Change Status Emojis

- 🟢 In Progress
- 🟡 Paused
- 🔴 Blocked
- ✅ Complete
- ⭐ High Priority

---

## Templates

### Daily Note Template

**Location:** `Templates/Daily Note Template.md`

**What you can customize:**
- Morning routine checklist
- Sections (add/remove as needed)
- Evening review questions
- Habit tracking

**Example additions:**
```markdown
## 💪 Workout
- [ ] Exercise completed

## 📚 Learning
What I learned today:
```

### Project Template

**Location:** `Templates/Project Template.md`

**What you can customize:**
- Project phases
- Deliverables tracking
- Revenue tracking
- Customer/client fields

---

## Automation Scripts

### Daily Note Creation

**File:** `.scripts/create_daily_note.sh`

**Customize the schedule:**
Edit the LaunchAgent plist (see Automation Guide.md)

**Customize the content:**
Edit `Templates/Daily Note Template.md`

### Metrics Update

**File:** `.scripts/update_metrics.py`

**Add custom metrics:**
```python
# Add after line 30
new_metric = input("Custom metric: ")
# Update your markdown files accordingly
```

---

## Folder Structure

### Add New Folders

Create folders for your specific needs:

```bash
mkdir Clients
mkdir Products
mkdir Marketing
mkdir Research
```

### Link from Dashboard

Add to Dashboard.md Quick Links:

```markdown
### Business
- [[Clients/Client Template]]
- [[Products/Product Template]]
```

---

## Quick Commands

### Add Custom Commands

Edit your `~/.zshrc` file:

```bash
# Obsidian Life Hub - Custom Commands
alias obs-weekly="python3 /path/to/vault/.scripts/weekly_review.py"
alias obs-client="python3 /path/to/vault/.scripts/new_client.py"
alias obs-backup="rsync -av /path/to/vault /path/to/backup"
```

Then reload:
```bash
source ~/.zshrc
```

---

## Visual Customization

### Obsidian Theme

1. Open Obsidian Settings
2. Appearance → Themes
3. Browse and install community themes
4. Recommended: Minimal, California Coast, Things

### CSS Snippets

Create `.obsidian/snippets/custom.css`:

```css
/* Custom dashboard styling */
.markdown-preview-view h1 {
  color: #6366f1;
  border-bottom: 2px solid #6366f1;
}

/* Revenue metrics highlight */
.markdown-preview-view h3:contains("MRR") {
  background: #10b981;
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
}
```

Enable in Settings → Appearance → CSS Snippets

---

## Plugins Recommendations

### Essential Community Plugins

**Dataview** (for advanced queries)
```dataview
TABLE status, mrr
FROM "Projects"
WHERE status = "in_progress"
SORT mrr DESC
```

**Templater** (advanced templates)
- Dynamic dates
- Auto-fill project names
- Smart variables

**Calendar** (visual date picker)
- Click to create/view daily notes
- See all notes on timeline

**Periodic Notes**
- Auto-create weekly/monthly notes
- Advanced scheduling

**Tasks** (advanced task management)
- Query tasks across all notes
- Due dates and priorities

### Install Plugins

1. Settings → Community plugins
2. Turn off Safe Mode
3. Browse and install
4. Enable installed plugins

---

## Data Export

### Backup Your Vault

**Automated backup script:**

Create `.scripts/backup_vault.sh`:
```bash
#!/bin/bash
VAULT_PATH="$HOME/path/to/vault"
BACKUP_PATH="$HOME/Dropbox/obsidian-backup"
rsync -av --delete "$VAULT_PATH/" "$BACKUP_PATH/"
echo "✅ Backup complete"
```

**Add to crontab (daily at midnight):**
```bash
0 0 * * * /path/to/vault/.scripts/backup_vault.sh
```

### Export to Other Formats

**Markdown → PDF:**
Use Obsidian's built-in PDF export

**Markdown → HTML:**
Use Obsidian Publish or static site generators

**Sync with Git:**
```bash
cd /path/to/vault
git init
git add .
git commit -m "Update"
git push
```

---

## Integration Ideas

### Zapier/n8n

**Trigger on new daily note:**
- Create calendar event
- Send Slack reminder
- Update project management tool

**Sync from external sources:**
- Import tasks from Todoist
- Pull GitHub issues
- Fetch Trello cards

### API Integrations

Add scripts in `.scripts/` to:
- Fetch data from APIs
- Update Obsidian notes automatically
- Push data to external services

**Example:** Stripe MRR sync
```python
import stripe
import os

stripe.api_key = os.getenv('STRIPE_KEY')
mrr = stripe.Subscription.list(status='active')
# Update Dashboard.md with real MRR
```

---

## Multi-Device Sync

### iCloud Drive
Move vault to `~/Library/Mobile Documents/iCloud~md~obsidian/`

### Dropbox
Move vault to `~/Dropbox/ObsidianVault/`

### Obsidian Sync (Paid)
Settings → Obsidian Sync → Enable

**Note:** Automation scripts work best on Mac/Linux. Mobile devices will have manual sync only.

---

## Advanced Customization

### Custom Metrics Dashboard

Create `Resources/Custom Metrics.md`:
```markdown
## Business Metrics
- CAC (Customer Acquisition Cost): $X
- LTV (Lifetime Value): $Y
- Churn Rate: Z%

## Personal Metrics
- Hours worked this week: X
- Deep work sessions: Y
- Books read this month: Z
```

### Weekly/Monthly Templates

Create templates for longer periods:
- `Templates/Weekly Review Template.md`
- `Templates/Monthly Review Template.md`
- `Templates/Quarterly Planning Template.md`

---

## Getting Help

- **Obsidian Forum:** https://forum.obsidian.md
- **Obsidian Discord:** https://discord.gg/obsidianmd
- **Obsidian Help:** https://help.obsidian.md

---

**Pro Tip:** Start with the default setup and customize gradually. Don't over-engineer at the beginning!
