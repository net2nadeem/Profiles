#!/usr/bin/env python3
"""
DamaDam Profile Scraper - SIMPLIFIED VERSION
No duplicate handling, new records at top, cell-level highlighting
"""

import os
import sys
import time
import json
import random
import re
from datetime import datetime

print("🚀 Starting DamaDam Scraper (Simplified Version)...")

# Check required packages
missing_packages = []

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    from webdriver_manager.chrome import ChromeDriverManager
    print("✅ Selenium ready")
except ImportError:
    missing_packages.append("selenium webdriver-manager")

try:
    import colorama
    from colorama import Fore, Style
    colorama.init(autoreset=True)
    print("✅ Colors ready")
except ImportError:
    missing_packages.append("colorama")
    class Fore:
        CYAN = GREEN = YELLOW = RED = WHITE = MAGENTA = BLUE = ""
    class Style:
        RESET_ALL = ""

try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    print("✅ Google Sheets ready")
except ImportError:
    missing_packages.append("gspread oauth2client")

if missing_packages:
    print(f"❌ Missing packages: {missing_packages}")
    sys.exit(1)

# === CONFIGURATION ===
LOGIN_URL = "https://damadam.pk/login/"
ONLINE_USERS_URL = "https://damadam.pk/online_kon/"

# Environment variables
USERNAME = os.getenv('DAMADAM_USERNAME')
PASSWORD = os.getenv('DAMADAM_PASSWORD')
SHEET_URL = os.getenv('GOOGLE_SHEET_URL')

if not all([USERNAME, PASSWORD, SHEET_URL]):
    print("❌ Missing required environment variables!")
    print("Required: DAMADAM_USERNAME, DAMADAM_PASSWORD, GOOGLE_SHEET_URL")
    sys.exit(1)

# Optimized delays
MIN_DELAY = 1.0
MAX_DELAY = 2.0
LOGIN_DELAY = 4
PAGE_LOAD_TIMEOUT = 8

# Tags configuration
TAGS_CONFIG = {
    'Following': '🔗 Following',
    'Followers': '⭐ Followers', 
    'Bookmark': '🔖 Bookmark',
    'Pending': '⏳ Pending'
}

# Highlight color for changed cells only
HIGHLIGHT_COLOR = {
    "red": 1.0,
    "green": 0.9,
    "blue": 0.6
}

# === LOGGING ===
def log_msg(message, level="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    colors = {"INFO": Fore.WHITE, "SUCCESS": Fore.GREEN, "WARNING": Fore.YELLOW, "ERROR": Fore.RED}
    color = colors.get(level, Fore.WHITE)
    print(f"{color}[{timestamp}] {level}: {message}{Style.RESET_ALL}")

# === STATS TRACKING ===
class ScraperStats:
    def __init__(self):
        self.start_time = datetime.now()
        self.total = self.current = self.success = self.errors = 0
        self.new_profiles = self.updated_cells = 0
        self.tags_processed = 0
    
    def show_summary(self):
        elapsed = str(datetime.now() - self.start_time).split('.')[0]
        print(f"\n{Fore.MAGENTA}📊 FINAL SUMMARY:")
        print(f"⏱️  Total Time: {elapsed}")
        print(f"👥 Users Found: {self.total}")
        print(f"✅ Successfully Scraped: {self.success}")
        print(f"❌ Errors: {self.errors}")
        print(f"🆕 New Profiles: {self.new_profiles}")
        print(f"🔄 Updated Cells: {self.updated_cells}")
        print(f"🏷️  Tags Processed: {self.tags_processed}{Style.RESET_ALL}")
        print("-" * 50)

stats = ScraperStats()

# === (browser setup, login_to_damadam, get_online_users, scrape_profile, clean_text, extract_numbers, get_google_sheets_client, get_tags_mapping, get_tags_for_nickname) ===
# unchanged from your version

# === GOOGLE SHEETS OPERATIONS ===
def export_to_google_sheets(profiles_batch, tags_mapping):
    """SIMPLIFIED Google Sheets export - no duplicates, top insertion, cell highlighting"""
    if not profiles_batch:
        return False
        
    try:
        log_msg(f"📊 Processing {len(profiles_batch)} profiles for Google Sheets...", "INFO")
        
        client = get_google_sheets_client()
        if not client:
            return False
            
        workbook = client.open_by_url(SHEET_URL)
        worksheet = workbook.sheet1
        
        # Setup headers (DATETIME combined)
        headers = ["DATETIME","NICKNAME","TAGS","CITY","GENDER","MARRIED","AGE",
                   "JOINED","FOLLOWERS","POSTS","PLINK","PIMAGE","INTRO"]
        
        existing_data = worksheet.get_all_values()
        if not existing_data or not existing_data[0]: 
            worksheet.append_row(headers)
            log_msg("✅ Headers added to Google Sheet", "SUCCESS")
            existing_rows = {}
        else:
            # Create mapping of nickname to row data and position
            existing_rows = {}
            for i, row in enumerate(existing_data[1:], 2):  # Skip header, start from row 2
                if len(row) > 1 and row[1].strip():  # Nickname is column B now
                    existing_rows[row[1].strip()] = {
                        'row_index': i,
                        'data': row
                    }
        
        new_count = 0
        updated_cells_count = 0
        
        for profile in profiles_batch:
            nickname = profile.get("NICKNAME","").strip()
            if not nickname: 
                continue
            
            # Add tags to profile
            profile['TAGS'] = get_tags_for_nickname(nickname, tags_mapping)
            
            # Prepare row data
            row = [
                profile.get("DATETIME",""),
                nickname,
                profile.get("TAGS",""),
                profile.get("CITY",""),
                profile.get("GENDER",""),
                profile.get("MARRIED",""),
                profile.get("AGE",""),
                profile.get("JOINED",""),
                profile.get("FOLLOWERS",""),
                profile.get("POSTS",""),
                profile.get("PLINK",""),
                profile.get("PIMAGE",""),
                clean_text(profile.get("INTRO",""))
            ]
            
            if nickname in existing_rows:
                # Update existing profile - only changed cells
                existing_info = existing_rows[nickname]
                row_index = existing_info['row_index']
                existing_data = existing_info['data']
                
                # Column mapping for letters
                col_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
                
                # Check each field and update only if different
                updated_any = False
                for col_idx, new_value in enumerate(row):
                    existing_value = existing_data[col_idx] if col_idx < len(existing_data) else ""
                    
                    # Always update DATETIME (column A)
                    if col_idx == 0:  
                        if existing_value != new_value:
                            cell_range = f"{col_letters[col_idx]}{row_index}"
                            worksheet.update(cell_range, new_value)
                            updated_any = True
                    
                    # Update other fields only if new value exists and is different
                    elif new_value and existing_value != new_value:
                        cell_range = f"{col_letters[col_idx]}{row_index}"
                        worksheet.update(cell_range, new_value)
                        
                        # Highlight only the changed cell
                        worksheet.format(cell_range, {
                            "backgroundColor": HIGHLIGHT_COLOR
                        })
                        
                        updated_cells_count += 1
                        stats.updated_cells += 1
                        updated_any = True
                        log_msg(f"🔄 Updated {nickname} - {headers[col_idx]}: {new_value}", "INFO")
                
                if not updated_any:
                    log_msg(f"➡️ {nickname} - No changes needed", "INFO")
                    
            else:
                # Add new profile AT THE TOP (row 2, after headers)
                try:
                    worksheet.insert_row(row, 2)
                    new_count += 1
                    stats.new_profiles += 1
                    log_msg(f"✅ Added new profile at top: {nickname}", "SUCCESS")
                except Exception as e:
                    log_msg(f"❌ Failed to add {nickname}: {e}", "ERROR")
        
        log_msg(f"📊 Export complete: {new_count} new, {updated_cells_count} cells updated", "SUCCESS")
        return True
        
    except Exception as e:
        log_msg(f"❌ Google Sheets export failed: {e}", "ERROR")
        return False

# === MAIN EXECUTION ===
def main():
    """Simplified main execution"""
    log_msg("🚀 Starting DamaDam Profile Scraper (Simplified)", "INFO")
    driver = setup_github_browser()
    if not driver:
        log_msg("❌ Failed to setup browser", "ERROR")
        return
    try:
        if not login_to_damadam(driver):
            log_msg("❌ Authentication failed", "ERROR")
            return
        client = get_google_sheets_client()
        if not client:
            log_msg("❌ Failed to connect to Google Sheets", "ERROR")
            return
        tags_mapping = get_tags_mapping(client, SHEET_URL)
        users = get_online_users(driver)
        if not users:
            log_msg("❌ No online users found", "ERROR")
            return
        stats.total = len(users)
        scraped_profiles = []
        batch_size = 10
        for i, nickname in enumerate(users, 1):
            stats.current = i
            log_msg(f"🔍 Scraping {nickname} ({i}/{stats.total})", "INFO")
            profile = scrape_profile(driver, nickname)
            if profile:
                scraped_profiles.append(profile)
                stats.success += 1
                if len(scraped_profiles) >= batch_size:
                    export_to_google_sheets(scraped_profiles, tags_mapping)
                    scraped_profiles = []
            else:
                stats.errors += 1
            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        if scraped_profiles:
            export_to_google_sheets(scraped_profiles, tags_mapping)
        stats.show_summary()
    except KeyboardInterrupt:
        log_msg("⏹️ Scraping interrupted by user", "WARNING")
    except Exception as e:
        log_msg(f"❌ Execution error: {e}", "ERROR")
    finally:
        try:
            driver.quit()
        except:
            pass
        log_msg("🏁 Scraper completed", "INFO")

if __name__ == "__main__":
    main()
