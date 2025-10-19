# Quick Start Guide

Get up and running with Obsidian Life Hub in 15 minutes.

---

## 🚀 Step 1: Install (2 min)

### Mac/Linux
```bash
cd /path/to/obsidian-life-hub
./install.sh
```

### Windows
```cmd
install.bat
```

**What this does:**
- Makes scripts executable
- Adds quick commands to your shell
- Sets up automatic daily notes (macOS)
- Tests installation

---

## 📱 Step 2: Open in Obsidian (1 min)

1. Open Obsidian app
2. Click "Open folder as vault"
3. Select the `obsidian-life-hub` folder
4. Click "Trust author and enable plugins" (if asked)

✅ Your vault is now loaded!

---

## 🎯 Step 3: First Daily Note (30 sec)

**Restart your terminal**, then:
```bash
obs-daily
```

This creates today's daily note from the template.

**Or:** Daily notes auto-create at 7 AM (macOS)

---

## 📊 Step 4: Explore Dashboard (2 min)

1. Open `Dashboard.md`
2. Right-click → "Pin" (keeps it accessible)
3. This is your home base!

**What's in the dashboard:**
- Revenue tracking
- Active projects
- This week's goals
- Quick links

---

## ⚙️ Step 5: Customize (5 min)

### Set Your Goal
Edit `Resources/Revenue Tracker.md`:
- Change goal amount
- Add your revenue streams
- Set weekly targets

### Add Your First Project
1. Copy `Templates/Project Template.md`
2. Create new note in `Projects/`
3. Fill in your project details
4. Link from Dashboard

---

## 💰 Step 6: Track Metrics (2 min)

When you make progress:
```bash
obs-metrics
```

**Update:**
- Revenue & MRR
- Customer count
- Activity logging

Dashboard updates automatically!

---

## 📧 Optional: Email/Calendar Sync (15 min)

See: `Resources/Sync Setup Guide.md`

**Benefits:**
- Important emails → Obsidian notes
- Calendar events → Daily notes
- Inbox zero workflow

---

## ⚡ Quick Commands Reference

```bash
obs-daily          # Create/open today's note
obs-metrics        # Update revenue/metrics
obs-sync-email     # Sync Gmail (after setup)
obs-sync-cal       # Sync calendar (after setup)
obs-open           # Open dashboard
obs-vault          # Go to vault directory
```

---

## 📅 Daily Workflow

### Morning
1. Daily note auto-opens at 7 AM (or run `obs-daily`)
2. Fill in top 3 priorities
3. Review calendar events (if synced)
4. Check dashboard

### During Day
- Check off tasks
- Add notes/ideas
- Log wins in real-time

### Evening
1. Review what you accomplished
2. Update metrics: `obs-metrics`
3. Set tomorrow's priorities

---

## 🎨 Recommended Plugins

Install from Obsidian → Settings → Community Plugins:

**Essential:**
- **Dataview** - Dynamic tables & queries
- **Calendar** - Visual calendar view
- **Templater** - Advanced templates

**Productivity:**
- **Tasks** - Task management across notes
- **Kanban** - Visual project boards

---

## 🛠️ Troubleshooting

### Commands don't work
```bash
# Reload shell config
source ~/.zshrc  # or ~/.bashrc

# Or restart terminal
```

### Daily note not auto-creating
```bash
# Check LaunchAgent (macOS)
launchctl list | grep obsidian

# Or create manually
obs-daily
```

### Can't find vault in Obsidian
Make sure you're opening the folder that contains:
- Dashboard.md
- Projects/
- Daily/
- etc.

---

## 📚 Learn More

- [[Automation Guide]] - Full automation details
- [[Sync Setup Guide]] - Email/calendar integration
- [[Customization Guide]] - Make it yours

---

## 🎯 Success in First Week

- [ ] Open Obsidian daily
- [ ] Create daily notes 5/7 days
- [ ] Update metrics at least once
- [ ] Add your first project
- [ ] Link related notes

**You'll know it's working when:**
- Dashboard is your daily starting point
- You check it every morning
- Projects are tracked in one place
- Find anything in < 10 seconds

---

## 🚀 Ready to Go!

You're all set up! Here's what to do right now:

1. ✅ Obsidian is open
2. ✅ Dashboard is pinned
3. ✅ Today's note created
4. ✅ Top 3 priorities set
5. ✅ Start being productive!

**Welcome to your new productivity system!** ⚡
