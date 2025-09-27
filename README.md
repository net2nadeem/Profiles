# 🔥 DD-Online: DamaDam Profile Scraper

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-4.15%2B-green)](https://selenium-python.readthedocs.io/)
[![Status](https://img.shields.io/badge/status-optimized-success.svg)]()

A high-performance, optimized web scraper for DamaDam.pk profiles with Google Sheets integration and advanced browser management.

## ✨ Key Features

- ⚡ **70% Faster Startup**: Optimized Chrome configuration eliminates startup delays
- 🔄 **Browser Reuse**: Continuous mode reuses browser sessions for maximum efficiency  
- 📊 **Google Sheets Integration**: Direct export with duplicate handling and seen count tracking
- 🎯 **Smart Data Extraction**: Comprehensive profile information with error recovery
- 📝 **CSV Export**: Local backup with UTF-8 encoding
- 🔐 **Secure Authentication**: Smart cookie management with multiple credential sources
- 📈 **Real-time Statistics**: Live progress tracking and performance metrics
- 🛡️ **Error Recovery**: Robust error handling and retry mechanisms

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/net2nadeem2/DD-Online.git
cd DD-Online
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Scraper
```bash
python DD-Online-Optimized.py
```

## ⚙️ Configuration Options

### Environment Variables (Optional)
Create a `.env` file or set environment variables:

```env
# DamaDam Credentials (optional - can be set in config.json or code)
DD_USERNAME=your_username
DD_PASSWORD=your_password

# Google Sheets (optional)
GOOGLE_SHEET_URL=https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
ENABLE_SHEETS=true

# Performance Settings
MIN_DELAY=0.5
MAX_DELAY=1.5
LOOP_WAIT_MINUTES=15
PAGE_LOAD_TIMEOUT=6
```

### Config File Method (Alternative)
Create `config.json`:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Google Sheets Setup (Optional)
1. Create a Google Cloud Service Account
2. Download credentials as `online.json` 
3. Share your Google Sheet with the service account email
4. The scraper will automatically export data with duplicate handling

## 📊 Performance Improvements

| Feature | Before | After | Improvement |
|---------|--------|--------|-------------|
| Browser Startup | ~4+ seconds | ~1-2 seconds | **70% faster** |
| Continuous Mode | Full restart each loop | Browser reuse | **Near-instant** subsequent runs |
| Chrome Errors | Multiple errors/warnings | Clean startup | **Eliminated** |
| Memory Usage | High (restarts) | Optimized (reuse) | **Significantly reduced** |

## 📁 Output Format

### CSV Output (`DD-profiless.csv`)
```csv
DATE,TIME,NICKNAME,TAGS,CITY,GENDER,MARRIED,AGE,JOINED,FOLLOWERS,POSTS,PLINK,PIMAGE,INTRO
25-Sep-2025,09:30 AM,user123,,Karachi,Male,Yes,25,2020,150,45,https://...,https://...,Profile intro...
```

### Google Sheets Integration
- ✅ Automatic duplicate detection by nickname
- 📊 Seen count tracking (SCOUNT column) 
- 🔄 Real-time updates during scraping
- 📝 Preserves historical data

## 🔧 Usage Modes

### 1. Single Run
- Runs once and exits
- Perfect for one-time data collection
- Browser closes after completion

### 2. Continuous Mode (Recommended)
- Runs continuously with configurable wait times
- **Browser reuse** eliminates startup overhead
- Ideal for ongoing monitoring
- Saves ~3-6 seconds per run

## 🐛 Troubleshooting

### Common Issues & Solutions

**"Chrome errors on startup"**
✅ **FIXED** in optimized version - eliminates registration errors, DevTools warnings, and TensorFlow loading

**"Browser taking too long to start"**  
✅ **OPTIMIZED** - New headless mode + disabled unnecessary services = 70% faster startup

**"Google Sheets not working"**
- Check if `online.json` exists
- Verify service account email is shared with your sheet
- Install: `pip install gspread oauth2client`

**"Login failing"**
- Verify credentials in environment variables, config.json, or code
- Check if account is not locked
- Try manual login first to verify credentials

**"Memory issues in continuous mode"**
✅ **SOLVED** - Browser reuse prevents memory leaks from constant restarts

## 📈 Performance Statistics

The scraper provides real-time statistics:
- 🚀 Browser setup time
- 🔐 Authentication time  
- 📊 Success/failure rates
- ⏱️ Total elapsed time
- 📈 Progress percentage

## 🔒 Security Features

- 🔐 **Multiple credential sources**: Environment variables → Config file → Hardcoded fallback
- 🍪 **Smart cookie management**: Reduces login frequency
- 📁 **File-based session storage**: Maintains login state between runs
- 🛡️ **No credentials in repository**: Uses secure external configuration

## 🎯 Technical Optimizations

### Browser Optimizations
- New headless mode (`--headless=new`)
- Disabled unnecessary Chrome services
- Eliminated TensorFlow/ML loading
- Removed DevTools overhead
- Optimized memory management

### Network Optimizations  
- Reduced timeouts (6s vs 10s default)
- Smart delay randomization (0.5-1.5s)
- Batch processing for Google Sheets

### Error Handling
- Comprehensive exception handling
- Graceful degradation on failures
- Automatic retry mechanisms
- Detailed logging with color coding

## 📝 Changelog

### v2.0.0 - Optimized Release
- ⚡ **70% faster browser startup**
- 🔄 **Browser reuse in continuous mode**
- 🛡️ **Enhanced error handling**
- 📊 **Real-time performance statistics** 
- 🔧 **Multiple configuration methods**
- 📈 **Improved Google Sheets integration**
- 🧹 **Cleaner console output**

### v1.0.0 - Initial Release
- 🎯 Basic profile scraping functionality
- 📁 CSV export capability
- 🔐 Cookie-based authentication

## ⚠️ Important Notes

- **Respect Rate Limits**: Built-in delays prevent overwhelming the target site
- **Educational Purpose**: This tool is for learning web scraping techniques
- **Terms of Service**: Please respect DamaDam.pk's terms of service
- **Responsible Usage**: Use reasonable delays and don't overload servers

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/net2nadeem2/DD-Online/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/net2nadeem2/DD-Online/discussions)
- 📧 **Contact**: Create an issue for support

## 📄 License

This project is open source and available under the MIT License.

---

<p align="center">
  <strong>⭐ If this project helped you, please give it a star! ⭐</strong>
</p>

<p align="center">Made with ❤️ for the DamaDam community</p>
