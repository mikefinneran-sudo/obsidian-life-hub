#!/bin/bash

echo "🚀 Obsidian Life Hub - Installation"
echo "===================================="
echo ""

# Get vault path
VAULT_PATH="$(pwd)"
echo "📁 Installing in: $VAULT_PATH"
echo ""

# Make scripts executable
echo "⚙️  Making scripts executable..."
chmod +x .scripts/*.sh .scripts/*.py
echo "✅ Scripts ready"
echo ""

# Add shell aliases
echo "🔗 Setting up quick commands..."
SHELL_RC="${HOME}/.zshrc"
if [ -f "${HOME}/.bashrc" ]; then
    SHELL_RC="${HOME}/.bashrc"
fi

# Check if aliases already exist
if ! grep -q "obs-daily" "$SHELL_RC" 2>/dev/null; then
    cat >> "$SHELL_RC" << EOF

# Obsidian Life Hub Commands
alias obs-daily="${VAULT_PATH}/.scripts/create_daily_note.sh"
alias obs-metrics="python3 ${VAULT_PATH}/.scripts/update_metrics.py"
alias obs-sync-email="python3 ${VAULT_PATH}/.scripts/sync_gmail.py"
alias obs-sync-cal="python3 ${VAULT_PATH}/.scripts/sync_calendar.py"
alias obs-sync-all="obs-sync-email && obs-sync-cal"
alias obs-open="open -a Obsidian ${VAULT_PATH}/Dashboard.md"
alias obs-vault="cd ${VAULT_PATH}"
EOF
    echo "✅ Quick commands added to $SHELL_RC"
else
    echo "✅ Quick commands already configured"
fi
echo ""

# Set up LaunchAgent for auto daily notes (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Setting up automatic daily notes (macOS)..."

    PLIST="${HOME}/Library/LaunchAgents/com.obsidian.lifehub.dailynote.plist"

    cat > "$PLIST" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.obsidian.lifehub.dailynote</string>
    <key>ProgramArguments</key>
    <array>
        <string>${VAULT_PATH}/.scripts/create_daily_note.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

    launchctl load "$PLIST" 2>/dev/null
    echo "✅ Daily notes will auto-create at 7 AM"
else
    echo "ℹ️  Auto daily notes available on macOS"
    echo "   For other systems, run 'obs-daily' manually"
fi
echo ""

# Test installation
echo "🧪 Testing installation..."
if command -v obs-daily &> /dev/null; then
    echo "✅ Quick commands work!"
else
    echo "⚠️  Quick commands need terminal restart"
    echo "   Run: source $SHELL_RC"
fi
echo ""

# Check Python packages for email/calendar sync
echo "📧 Checking email/calendar sync requirements..."
if python3 -c "import google.auth" 2>/dev/null; then
    echo "✅ Google API packages installed"
else
    echo "⚠️  Google API packages not installed"
    echo "   For email/calendar sync, run:"
    echo "   pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib"
fi
echo ""

# Final instructions
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Installation Complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Next Steps:"
echo ""
echo "1. Open Obsidian:"
echo "   - File → Open folder as vault"
echo "   - Select: $VAULT_PATH"
echo ""
echo "2. Open Dashboard.md (your home base)"
echo ""
echo "3. Create today's note:"
echo "   - Restart terminal (or run: source $SHELL_RC)"
echo "   - Run: obs-daily"
echo ""
echo "4. Optional - Set up email/calendar sync:"
echo "   - See: Resources/Sync Setup Guide.md"
echo ""
echo "⚡ Quick Commands:"
echo "   obs-daily      - Create today's note"
echo "   obs-metrics    - Update metrics"
echo "   obs-open       - Open dashboard"
echo ""
echo "📚 Documentation: Resources/ folder"
echo ""
echo "🚀 You're ready to go!"
echo ""
