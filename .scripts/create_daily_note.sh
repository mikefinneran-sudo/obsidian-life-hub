#!/bin/bash

# Auto-create daily note with template
# Run this every morning or on-demand

VAULT_PATH="$HOME/Documents/ObsidianVault"
DAILY_DIR="$VAULT_PATH/Daily"
TEMPLATE="$VAULT_PATH/Templates/Daily Note Template.md"
TODAY=$(date +%Y-%m-%d)
DAY_NAME=$(date +%A)
DAILY_NOTE="$DAILY_DIR/$TODAY.md"

# Check if today's note already exists
if [ -f "$DAILY_NOTE" ]; then
    echo "✅ Daily note for $TODAY already exists"
    open "obsidian://open?vault=ObsidianVault&file=Daily/$TODAY"
    exit 0
fi

# Create daily note from template
cat "$TEMPLATE" | sed "s/{{date:YYYY-MM-DD}}/$TODAY/g" | sed "s/{{date:dddd}}/$DAY_NAME/g" > "$DAILY_NOTE"

echo "✨ Created daily note for $TODAY"
echo "📝 Opening in Obsidian..."

# Open in Obsidian
open "obsidian://open?vault=ObsidianVault&file=Daily/$TODAY"
