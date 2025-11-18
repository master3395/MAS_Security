#!/usr/bin/env python3
"""
Script to take screenshots of the MAS Security module pages
"""

import os
import sys
import time
from pathlib import Path

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError:
    print("Selenium not installed. Trying playwright...")
    try:
        from playwright.sync_api import sync_playwright
        USE_PLAYWRIGHT = True
    except ImportError:
        print("Neither selenium nor playwright is installed.")
        print("Please install one of them:")
        print("  pip install selenium")
        print("  OR")
        print("  pip install playwright && playwright install")
        sys.exit(1)
else:
    USE_PLAYWRIGHT = False

# Create images directory if it doesn't exist
images_dir = Path(__file__).parent / "images"
images_dir.mkdir(exist_ok=True)

urls = [
    ("https://newstargeted.com/vulnerability-disclosure", "vulnerability-disclosure.png"),
    ("https://newstargeted.com/security-acknowledgments", "security-acknowledgments.png"),
]

def take_screenshot_selenium(url, filename):
    """Take screenshot using Selenium"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        # Wait for page to load
        time.sleep(3)
        
        # Scroll to ensure all content is loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
        # Take screenshot
        filepath = images_dir / filename
        driver.save_screenshot(str(filepath))
        print(f"Screenshot saved: {filepath}")
        
        driver.quit()
        return True
    except Exception as e:
        print(f"Error with Selenium: {e}")
        return False

def take_screenshot_playwright(url, filename):
    """Take screenshot using Playwright"""
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1920, "height": 1080})
            
            # Set longer timeout and use 'load' instead of 'networkidle'
            page.goto(url, wait_until="load", timeout=60000)
            
            # Wait a bit for any dynamic content
            page.wait_for_timeout(3000)
            
            # Scroll to ensure all content is loaded
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(1000)
            
            # Take screenshot
            filepath = images_dir / filename
            page.screenshot(path=str(filepath), full_page=True)
            print(f"Screenshot saved: {filepath}")
            
            browser.close()
            return True
        except Exception as e:
            print(f"Error with Playwright: {e}")
            return False

def main():
    print("Taking screenshots...")
    print(f"Output directory: {images_dir}")
    
    success_count = 0
    
    for url, filename in urls:
        print(f"\nCapturing: {url}")
        
        if USE_PLAYWRIGHT:
            success = take_screenshot_playwright(url, filename)
        else:
            success = take_screenshot_selenium(url, filename)
        
        if success:
            success_count += 1
    
    print(f"\n{'='*50}")
    if success_count == len(urls):
        print(f"Successfully captured {success_count} screenshots!")
        print(f"  Location: {images_dir}")
    else:
        print(f"Captured {success_count}/{len(urls)} screenshots")
        print("  Some screenshots may have failed. Check errors above.")

if __name__ == "__main__":
    main()

