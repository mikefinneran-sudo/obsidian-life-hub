#!/usr/bin/env python3
"""
Auto-update metrics in Obsidian vault
Tracks revenue, customers, outreach, etc.
"""

import os
import re
from datetime import datetime, date
from pathlib import Path

VAULT_PATH = Path.home() / "Documents" / "ObsidianVault"
REVENUE_FILE = VAULT_PATH / "Resources" / "Revenue Goals.md"
DASHBOARD_FILE = VAULT_PATH / "Dashboard.md"
WALTERFETCH_FILE = VAULT_PATH / "Projects" / "WalterFetch.md"

def update_revenue_metrics(mrr=0, customers=0, notes=""):
    """Update revenue tracking table"""
    if not REVENUE_FILE.exists():
        print(f"❌ Revenue file not found: {REVENUE_FILE}")
        return

    content = REVENUE_FILE.read_text()
    today = date.today().strftime("%Y-%m-%d")
    daily_avg = round(mrr / 30, 2) if mrr > 0 else 0

    # Add new row to tracking table
    table_line = f"| {today} | {customers} | 0 | ${mrr} | ${daily_avg} | {notes} |"

    # Find table and append
    if "| Date | New Customers" in content:
        # Replace the empty row
        content = re.sub(
            r'\|\s+\|\s+\|\s+\|\s+\|\s+\|',
            table_line,
            content,
            count=1
        )
        REVENUE_FILE.write_text(content)
        print(f"✅ Updated revenue metrics: ${mrr} MRR, {customers} customers")
    else:
        print("⚠️  Could not find tracking table")

def update_dashboard(mrr=0, customers=0):
    """Update dashboard with current metrics"""
    if not DASHBOARD_FILE.exists():
        print(f"❌ Dashboard not found: {DASHBOARD_FILE}")
        return

    content = DASHBOARD_FILE.read_text()

    # Update MRR
    content = re.sub(r'### Current MRR: \$\d+', f'### Current MRR: ${mrr}', content)

    # Update progress bar (based on $3000 goal)
    progress_pct = min(100, round((mrr / 3000) * 100))
    filled = round(progress_pct / 10)
    empty = 10 - filled
    progress_bar = '⬛' * filled + '⬜' * empty

    content = re.sub(
        r'\*\*Progress:\*\* [⬛⬜]+\s+\d+%',
        f'**Progress:** {progress_bar} {progress_pct}%',
        content
    )

    # Update customer count
    content = re.sub(
        r'\| Customers \| \d+ \|',
        f'| Customers | {customers} |',
        content
    )

    # Update daily average
    daily_avg = round(mrr / 30, 2)
    content = re.sub(
        r'\| Daily Avg \| \$[\d.]+ \|',
        f'| Daily Avg | ${daily_avg} |',
        content
    )

    DASHBOARD_FILE.write_text(content)
    print(f"✅ Updated dashboard: ${mrr} MRR, {customers} customers, {progress_pct}% to goal")

def log_activity(activity_type, count, notes=""):
    """Log daily activities (outreach, calls, etc.)"""
    today_file = VAULT_PATH / "Daily" / f"{date.today().strftime('%Y-%m-%d')}.md"

    if not today_file.exists():
        print(f"⚠️  Today's daily note doesn't exist yet. Run create_daily_note.sh first.")
        return

    content = today_file.read_text()

    # Update metrics section
    if activity_type == "outreach":
        content = re.sub(
            r'\*\*New Leads:\*\* \d+',
            f'**New Leads:** {count}',
            content
        )
    elif activity_type == "conversations":
        content = re.sub(
            r'\*\*Conversations:\*\* \d+',
            f'**Conversations:** {count}',
            content
        )

    # Add to notes if provided
    if notes:
        notes_section = f"\n- {activity_type.title()}: {notes}\n"
        content = content.replace("## 💡 Ideas & Notes\n\n-", f"## 💡 Ideas & Notes\n{notes_section}")

    today_file.write_text(content)
    print(f"✅ Logged {activity_type}: {count}")

def main():
    print("📊 Obsidian Metrics Updater\n")
    print("Choose an action:")
    print("1. Update revenue metrics")
    print("2. Log outreach activity")
    print("3. Log conversations")
    print("4. Quick update (manual entry)")

    choice = input("\nChoice (1-4): ").strip()

    if choice == "1":
        mrr = int(input("Current MRR: $"))
        customers = int(input("Total customers: "))
        notes = input("Notes (optional): ")
        update_revenue_metrics(mrr, customers, notes)
        update_dashboard(mrr, customers)

    elif choice == "2":
        count = int(input("Number of outreach messages sent: "))
        notes = input("Notes (optional): ")
        log_activity("outreach", count, notes)

    elif choice == "3":
        count = int(input("Number of conversations: "))
        notes = input("Notes (optional): ")
        log_activity("conversations", count, notes)

    elif choice == "4":
        print("\n📝 Quick manual update:")
        mrr = int(input("MRR: $"))
        customers = int(input("Customers: "))
        update_dashboard(mrr, customers)
        update_revenue_metrics(mrr, customers, "Quick update")
        print("\n✨ All metrics updated!")

    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
