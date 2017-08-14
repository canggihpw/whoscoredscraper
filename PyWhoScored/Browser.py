# -*- coding: utf-8 -*-
"""
Browser.py
Managing handler of web browsers
---
USAGE:
# import the class
from WhoScored import WhoScoredScraper
# create instance
ws = WhoScoredScrapper(<browsertype>)
# browsertype:
# 0 - Chrome
# 1 - Firefox
# 2 - Safari
# 3 - Opera
# 4 - Edge
---
"""

from __future__ import division
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#currURL = "https://www.whoscored.com/"

def get_handler(browserType):
    try:        
        # Load driver
        if browserType == 0:
            browser = webdriver.Chrome()
        elif browserType == 1:
            browser = webdriver.Firefox()
        elif browserType == 2:
            browser = webdriver.Safari()
        elif browserType == 3:
            browser = webdriver.Opera()
        elif browserType == 4:
            browser = webdriver.Edge()
        else:
            browser = webdriver.Chrome()
    except Exception:
        print Exception.message
    return browser

# Method to open the browser.
# Here I use Chrome, for other browsers can be seen in Selenium websites
def open_browser(handler,url):
    try:
        # Load page
        handler.get(url)
        # Wait until certain element is visible
        try:
            checkelem = WebDriverWait(handler,10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"body"))
#            EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div#footer-wslogo"))
            )
        except Exception:
            return False
            print Exception.message
            quit_browser(handler)

    except Exception:
        return False
        print Exception.message
        quit_browser(handler)

    finally:
        return True
#        htmldata = handler.find_elements_by_css_selector("body")[0].get_attribute("innerHTML")
        
# Close Chrome application
def quit_browser(handler):
    handler.quit()