# GitHub Contribution Heatmap Widget

A minimal, draggable GTK4 widget that displays your GitHub contribution graph.

## Features

✨ **Minimal Design** - Just the heatmap, no clutter  
🎯 **Draggable** - Move it anywhere on your desktop  
💾 **Remembers Username** - Auto-loads next time you open it  
🔄 **Easy to Change** - Open the app to edit username  
🌐 **Fetches from GitHub** - Real contribution data  

## Installation

### Requirements
- Python 3.7+
- GTK 4
- `curl` (for fetching data)

### On Linux (Fedora/RHEL)
```bash
sudo dnf install python3 gtk4
```

### On Linux (Ubuntu/Debian)
```bash
sudo apt install python3 libgtk-4-1
```

### On macOS
```bash
brew install gtk4
```

## Usage

### First Time
Run the application:
```bash
python3 heatmap.py
```

A dialog will appear asking for your GitHub username. Enter it and click OK.

### Subsequent Times
Just run the same command - it will auto-load your saved username!

### Change Username
Simply open the app and close the username dialog - no wait, just modify the command with your new username or delete the config file:
```bash
rm ~/.github-heatmap/config.json
```

Then run again and enter a new username.

## File Structure

```
.
├── heatmap.py              # Main application (run this!)
├── config.py               # Configuration manager
├── github_fetcher.py       # GitHub data fetcher
├── heatmap_widget.py       # Heatmap display widget
├── username_dialog.py      # Username input dialog
└── README.md              # This file
```

## How It Works

1. **First Run**: App asks for your GitHub username
2. **Save**: Username is saved to `~/.github-heatmap/config.json`
3. **Fetch**: App fetches your contribution data from GitHub
4. **Display**: Shows a beautiful heatmap widget
5. **Next Run**: Auto-loads saved username, shows heatmap immediately

## Configuration

Username is saved in: `~/.github-heatmap/config.json`

To reset, delete this file and the app will ask for username again.

## Keyboard Shortcuts

- **Enter**: In the username dialog, press Enter to submit
- **Escape**: Close dialogs

## Tips

- The widget is draggable - just grab the title bar and move it anywhere
- Hover over squares to see the date and contribution level
- Color intensity shows contribution level (gray = none, dark green = many)
- Window is resizable if you need to adjust the size

## Troubleshooting

### "Could not fetch data"
- Check your internet connection
- Make sure the username is correct (case-sensitive)
- Try a known username like `torvalds` to test

### "No commits found"
- This means the GitHub API returned no data
- This can happen if the profile is private or brand new

### Config not saving
- Make sure `~/.github-heatmap/` directory exists
- Check file permissions in home directory

## License

Free to use and modify!