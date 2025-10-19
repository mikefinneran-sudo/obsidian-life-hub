# Testing Checklist

Use this checklist to verify your Obsidian Life Hub installation works correctly.

---

## ✅ Installation Test (5 minutes)

### 1. Extract & Locate
- [ ] Unzipped file successfully
- [ ] Moved to desired location (e.g., `~/Documents/ObsidianLifeHub`)
- [ ] Can navigate to folder in Finder/Terminal

### 2. Run Installation
```bash
cd ~/Documents/ObsidianLifeHub
./install.sh
```

**Expected Output:**
```
🚀 Obsidian Life Hub - Installation
====================================
⚙️  Making scripts executable...
✅ Scripts ready
🔗 Setting up quick commands...
✅ Quick commands added to /Users/yourname/.zshrc
🍎 Setting up automatic daily notes (macOS)...
✅ Daily notes will auto-create at 7 AM
🧪 Testing installation...
⚠️  Quick commands need terminal restart
   Run: source /Users/yourname/.zshrc
📧 Checking email/calendar sync requirements...
⚠️  Google API packages not installed
✨ Installation Complete!
```

- [ ] Installation completed without errors
- [ ] Saw all success checkmarks (✅)

---

## ✅ Obsidian App Test (5 minutes)

### 3. Open Vault in Obsidian

1. Open Obsidian application
2. File → Open folder as vault
3. Select your vault folder
4. Should see Dashboard.md open automatically (or open it manually)

**Check the following:**
- [ ] Dashboard.md loads without errors
- [ ] All sections visible (Revenue Dashboard, Active Projects, etc.)
- [ ] Emoji icons display correctly
- [ ] No broken wiki links (should be purple/clickable, not gray)

### 4. Test Wiki Links

Click each link in Dashboard and verify the file opens:
- [ ] [[Daily Note Template]]
- [ ] [[Goals & Milestones]]
- [ ] [[Habits & Routines]]
- [ ] [[Revenue Tracker]]
- [ ] [[Project Template]]
- [ ] [[Customer Template]]
- [ ] [[Quick Start Guide]]
- [ ] [[Automation Guide]]
- [ ] [[Customization Guide]]
- [ ] [[Example Project]]

**All links should open a file. If any link is gray/unclickable, report an issue.**

---

## ✅ Automation Test (10 minutes)

### 5. Test Quick Commands

**Restart your terminal first:**
```bash
# Close and reopen Terminal, OR run:
source ~/.zshrc
```

**Test each command:**

#### A. Create Daily Note
```bash
obs-daily
```
- [ ] Command runs without errors
- [ ] Opens Obsidian to today's note
- [ ] Note is in `Daily/YYYY-MM-DD.md` format
- [ ] Contains today's date

#### B. Update Metrics
```bash
obs-metrics
```
- [ ] Command runs
- [ ] Prompts for MRR (enter 0 for testing)
- [ ] Prompts for customers (enter 0)
- [ ] Optional notes (press Enter to skip)
- [ ] Shows success message
- [ ] Dashboard.md updated with test data

#### C. Open Dashboard
```bash
obs-open
```
- [ ] Opens Obsidian
- [ ] Opens Dashboard.md
- [ ] No errors

#### D. Navigate to Vault
```bash
obs-vault
pwd
```
- [ ] Changes directory to vault
- [ ] Shows vault path

---

## ✅ Templates Test (5 minutes)

### 6. Test Daily Note Template

```bash
obs-daily
```

Open today's note in Obsidian and verify it contains:
- [ ] Today's date in title
- [ ] Day of week (e.g., "Saturday")
- [ ] Sections: Priorities, Wins, Projects, Notes
- [ ] Quick Commands section at bottom
- [ ] Formatted correctly (no weird placeholders)

### 7. Test Project Template

1. In Obsidian, create new note in `Projects/` folder
2. Name it "Test Project"
3. Copy contents from `Templates/Project Template.md`
4. Paste into your new note

Check:
- [ ] All sections present (Overview, Timeline, Revenue, etc.)
- [ ] Placeholders like {{Project Name}} are there
- [ ] No formatting errors

### 8. Test Customer Template

Same as above but with `Templates/Customer Template.md`:
- [ ] Contact Information section
- [ ] Communication Log
- [ ] Revenue tracking table
- [ ] All fields present

---

## ✅ Automation Schedule Test (Optional)

### 9. Test Automatic Daily Notes (macOS only)

**Check if LaunchAgent is running:**
```bash
launchctl list | grep obsidian
```

Expected output:
```
com.obsidian.lifehub.dailynote
```

- [ ] LaunchAgent is listed
- [ ] No error messages

**To test immediately:**
```bash
launchctl start com.obsidian.lifehub.dailynote
```
- [ ] Daily note created (or message that it already exists)

---

## ✅ Documentation Test (5 minutes)

### 10. Verify All Documentation Exists

Check these files exist and open correctly:
- [ ] README.md
- [ ] Resources/Quick Start Guide.md
- [ ] Resources/Automation Guide.md
- [ ] Resources/Customization Guide.md
- [ ] Resources/Revenue Tracker.md
- [ ] Resources/Goals & Milestones.md
- [ ] Resources/Habits & Routines.md

### 11. Read Quick Start Guide

Open `Resources/Quick Start Guide.md` in Obsidian:
- [ ] Instructions are clear
- [ ] All steps make sense
- [ ] No typos or broken formatting
- [ ] Example commands look correct

---

## 🎯 Final Verification

### Overall Check
- [ ] All commands work without errors
- [ ] All wiki links work in Obsidian
- [ ] Templates are correctly formatted
- [ ] Documentation is readable
- [ ] Daily notes auto-create (or manual command works)
- [ ] Metrics tracking works

### Known Limitations
- Email/calendar sync requires additional setup (see Automation Guide)
- Windows users need manual setup (no auto LaunchAgent)
- Some commands need terminal restart after install

---

## 🐛 Found an Issue?

If anything doesn't work as expected:

1. **Check installation logs** - Did `install.sh` show any errors?
2. **Verify file permissions** - Run: `ls -la .scripts/*.sh`
3. **Terminal restart** - Close and reopen Terminal
4. **Path issues** - Make sure you're in the vault directory

**Common Fixes:**
```bash
# Re-run installation
./install.sh

# Make scripts executable
chmod +x .scripts/*.sh .scripts/*.py

# Reload shell config
source ~/.zshrc

# Check LaunchAgent (macOS)
launchctl list | grep obsidian
```

---

## ✨ Success!

If all tests pass:
- **🎉 Your Obsidian Life Hub is ready to use!**
- Start customizing Dashboard.md with your projects
- Run `obs-daily` every morning to create your daily note
- Run `obs-metrics` weekly to track progress
- Explore all the templates and documentation

**Next Steps:**
1. Read `Resources/Customization Guide.md` to personalize your vault
2. Set up email/calendar sync (optional) - see `Resources/Automation Guide.md`
3. Start tracking your first project in `Projects/`

---

**Testing completed:** YYYY-MM-DD
**Version:** 1.0
**Platform:** macOS / Linux / Windows
