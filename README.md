# DamaDam Profile Scraper 🚀

An automated web scraper for DamaDam profiles with Google Sheets integration, designed to run on GitHub Actions with intelligent tagging and update systems.

## ✨ Features

- **🔗 Smart Tagging System**: Automatically tags users based on your predefined categories
- **🔄 Intelligent Updates**: Only updates changed data and highlights updated rows
- **🚫 Duplicate Prevention**: No more duplicate entries or unnecessary seen counts
- **☁️ Cloud Ready**: Optimized for GitHub Actions execution
- **📊 Google Sheets Integration**: Direct export to Google Sheets with formatting
- **🎯 Batch Processing**: Efficient batch operations to minimize API calls
- **📱 Mobile Optimized**: Works with mobile view layouts

## 🏷️ Tagging System

The scraper reads from a "Tags" sheet in your Google Sheets to automatically categorize users:

| Column A (Following) | Column B (Followers) | Column C (Bookmark) | Column D (Pending) |
|---------------------|---------------------|-------------------|-------------------|
| 🔗 Following       | ⭐ Followers        | 🔖 Bookmark       | ⏳ Pending        |

**Example Tags Output**: `🔗 Following, 🔖 Bookmark` for users found in multiple categories.

## 📊 Data Structure

### Main Sheet Columns:
| DATE | TIME | NICKNAME | TAGS | CITY | GENDER | MARRIED | AGE | JOINED | FOLLOWERS | POSTS | PLINK | PIMAGE | INTRO |

### Features:
- **Light Mustard Highlighting**: Updated rows are highlighted automatically
- **No Duplicates**: Smart update system prevents duplicate entries
- **All Field Updates**: Updates all fields when changes are detected

## 🚀 Quick Start

### 1. Fork This Repository
Click the "Fork" button to create your own copy of this repository.

### 2. Set Up Google Sheets

#### Create Your Sheets:
1. **Main Sheet**: Will store all profile data
2. **Tags Sheet**: Create with columns A-D for Following, Followers, Bookmark, Pending

#### Get Google Sheets API Credentials:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable "Google Sheets API" and "Google Drive API"
4. Create Service Account credentials
5. Download the JSON credentials file
6. Share your Google Sheet with the service account email

### 3. Configure GitHub Secrets

Go to your repository → Settings → Secrets and variables → Actions

Add these secrets:

```
DAMADAM_USERNAME=your_damadam_username
DAMADAM_PASSWORD=your_damadam_password  
GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
GOOGLE_SERVICE_ACCOUNT_JSON={"type":"service_account","project_id":"your-project",...}
```

### 4. Run the Scraper

#### Manual Trigger:
- Go to Actions tab → DamaDam Scraper → Run workflow

#### Automatic Schedule:
The workflow is set to run every 6 hours. Edit `.github/workflows/scraper.yml` to change the schedule.

## 🛠️ Local Development

### Prerequisites
```bash
pip install selenium webdriver-manager colorama gspread oauth2client
```

### Environment Setup
```bash
export DAMADAM_USERNAME="your_username"
export DAMADAM_PASSWORD="your_password"
export GOOGLE_SHEET_URL="your_sheet_url"
export GOOGLE_SERVICE_ACCOUNT_JSON='{"type":"service_account",...}'
```

### Run Locally
```bash
python scraper.py
```

## 📋 Requirements

- Python 3.8+
- Chrome/Chromium (automatically managed in GitHub Actions)
- Google Sheets with proper permissions
- DamaDam account credentials

## 🔧 Configuration

### Delays and Timeouts
```python
MIN_DELAY = 1.0          # Minimum delay between requests
MAX_DELAY = 2.0          # Maximum delay between requests
LOGIN_DELAY = 4          # Delay after login
PAGE_LOAD_TIMEOUT = 8    # Page load timeout
```

### Batch Processing
```python
batch_size = 10          # Profiles per batch for Google Sheets export
```

### Highlighting Color
```python
HIGHLIGHT_COLOR = {
    "red": 1.0,
    "green": 0.9,
    "blue": 0.6
}  # Light mustard
```

## 📈 Performance Optimizations

- **🎯 Batch Processing**: Reduces API calls to Google Sheets
- **🧠 Smart Updates**: Only updates when necessary
- **⚡ Optimized Selenium**: GitHub Actions specific browser settings
- **🔄 Efficient Tagging**: Cached tag mapping for better performance
- **📱 Mobile Selectors**: Multiple fallback selectors for reliability

## 🔍 Troubleshooting

### Common Issues:

#### 1. Login Failed
```
❌ Login failed - authentication unsuccessful
```
**Solution**: Check your DamaDam credentials in GitHub Secrets.

#### 2. Google Sheets Access Denied
```
❌ Failed to setup Google Sheets client
```
**Solution**: 
- Verify your service account JSON is correct
- Ensure the sheet is shared with service account email
- Check API permissions

#### 3. No Users Found
```
❌ No online users found
```
**Solution**: 
- Check if DamaDam is accessible
- Verify login was successful
- Try running at different times

#### 4. Tags Not Loading
```
⚠️ Tags sheet not found, skipping tags
```
**Solution**: 
- Create a sheet named "Tags" in your workbook
- Add columns: Following, Followers, Bookmark, Pending
- Add usernames in respective columns

## 📊 Sample Output

```
🚀 Starting DamaDam Scraper (Optimized Version)...
✅ Selenium ready
✅ Colors ready
✅ Google Sheets ready
🔐 Logging in to DamaDam...
✅ Login successful
🏷️ Loading tags mapping...
✅ Loaded tags for 45 users
👥 Fetching online users...
✅ Found 123 unique online users
🔍 Scraping user1 (1/123)
✅ Added new profile: user1
🔄 Updated user2 (highlighted)
📊 Export complete: 12 new, 8 updated

📊 FINAL SUMMARY:
⏱️  Total Time: 0:15:23
👥 Users Found: 123
✅ Successfully Scraped: 121
❌ Errors: 2
🆕 New Profiles: 12
🔄 Updated Profiles: 8
🏷️  Tags Processed: 45
```

## 🎨 Customization

### Adding New Tag Categories
1. Add new column in Tags sheet
2. Update `TAGS_CONFIG` in scraper.py:
```python
TAGS_CONFIG = {
    'Following': '🔗 Following',
    'Followers': '⭐ Followers', 
    'Bookmark': '🔖 Bookmark',
    'Pending': '⏳ Pending',
    'VIP': '👑 VIP',  # New category
}
```

### Changing Update Frequency
Edit `.github/workflows/scraper.yml`:
```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
  - cron: '0 */2 * * *'  # Every 2 hours (more frequent)
  - cron: '0 8,20 * * *' # Twice daily at 8 AM and 8 PM
```

### Custom Highlight Color
```python
HIGHLIGHT_COLOR = {
    "red": 0.9,    # Light green
    "green": 1.0,
    "blue": 0.9
}
```

## 📁 File Structure

```
damadam-scraper/
├── scraper.py                 # Main scraper script
├── requirements.txt           # Python dependencies
├── .github/
│   └── workflows/
│       └── scraper.yml       # GitHub Actions workflow
├── README.md                 # This file
├── .gitignore               # Git ignore file
└── samples/
    ├── sample-sheet.png     # Sample Google Sheet layout
    └── tags-example.png     # Tags sheet example
```

## 🔐 Security Best Practices

- ✅ Never commit credentials to repository
- ✅ Use GitHub Secrets for sensitive data
- ✅ Regularly rotate DamaDam password
- ✅ Monitor Google Sheets access logs
- ✅ Use least privilege for service account permissions

## 📝 Changelog

### v2.0.0 (Current)
- ✨ Added intelligent tagging system
- 🔄 Implemented smart update logic with highlighting
- 🚫 Removed duplicate entries and SCOUNT column
- ⚡ Performance optimizations for GitHub Actions
- 📱 Enhanced mobile selector support
- 🎨 Added light mustard highlighting for updates

### v1.0.0
- 🚀 Initial release with basic scraping
- 📊 Google Sheets integration
- 🔁 Duplicate counting system (deprecated)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This scraper is for educational purposes only. Please:
- Respect DamaDam's terms of service
- Use reasonable delays between requests
- Don't overload their servers
- Respect user privacy

## 🆘 Support

- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact repository owner for urgent matters

## 🙏 Acknowledgments

- **Selenium WebDriver** - For web automation
- **Google Sheets API** - For data storage
- **GitHub Actions** - For cloud automation
- **DamaDam Community** - For providing the platform

---

**⭐ If this project helped you, please give it a star!**

**📢 Found a bug or want a feature?** [Open an issue](../../issues/new)
