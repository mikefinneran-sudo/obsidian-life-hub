#!/bin/bash

# Auto-create daily note with template
# Run this every morning or on-demand

# Auto-detect vault path (script is in .scripts/ folder)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VAULT_PATH="$(dirname "$SCRIPT_DIR")"
VAULT_NAME="$(basename "$VAULT_PATH")"
DAILY_DIR="$VAULT_PATH/Daily"
TEMPLATE="$VAULT_PATH/Templates/Daily Note Template.md"
TODAY=$(date +%Y-%m-%d)
DAY_NAME=$(date +%A)
DAILY_NOTE="$DAILY_DIR/$TODAY.md"

# Create Daily folder if it doesn't exist
mkdir -p "$DAILY_DIR"

# Check if today's note already exists
if [ -f "$DAILY_NOTE" ]; then
    echo "✅ Daily note for $TODAY already exists"
    exit 0
fi

# Create daily note from template
cat "$TEMPLATE" | sed "s/{{date:YYYY-MM-DD}}/$TODAY/g" | sed "s/{{date:dddd}}/$DAY_NAME/g" > "$DAILY_NOTE"

echo "✨ Created daily note for $TODAY"
echo "📝 File: $DAILY_NOTE"
