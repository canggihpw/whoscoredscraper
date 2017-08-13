# -*- coding: utf-8 -*-
"""
WhoScored.py
A class for extracting WhoScored data
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
import WSTournamentList


class WhoScoredScraper:
    currURL = "https://www.whoscored.com/"
    
    def __init__(self,browser):
        try:        
            # Load driver
            if browser == 0:
                self._browser = webdriver.Chrome()
            elif browser == 1:
                self._browser = webdriver.Firefox()
            elif browser == 2:
                self._browser = webdriver.Safari()
            elif browser == 3:
                self._browser = webdriver.Opera()
            elif browser == 4:
                self._browser = webdriver.Edge()
            else:
                self._browser = webdriver.Chrome()
        except Exception:
            print Exception.message
    
    # Method to open the browser.
    # Here I use Chrome, for other browsers can be seen in Selenium websites
    def _open_browser(self):
        try:
            # Load page
            self._browser.get(self.currURL)
            # Wait until certain element is visible
            try:
                checkelem = WebDriverWait(self._browser,10).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"div#footer-wslogo"))
                )
            except Exception:
                print Exception.message
                self.quitBrowser()

        except Exception:
            print Exception.message
            self.quitBrowser()

    # Close Chrome application
    def quit_browser(self):
        self._browser.quit()

#    def getTournamentList(self):
#        #2-cols list. First col contains the name. Second col contains the url
#        self._tList = []
#        #Select list of tournaments
#        html = self._browser.find_elements_by_css_selector("ul#popular-tournaments-list>li")
#        for ht in html:
#            self._tList.append([ht.text,ht.find_element_by_tag_name("a").get_attribute("href")])
#        return self._tList

    # Get the current standing by searching element
    # URL of the tournament is extracted from WSTournamentList
    def get_current_table(self,idTournament):
        curtable = []
        self.currURL = WSTournamentList.TournamentLists[idTournament][2]
        self._open_browser()

        html = self._browser.find_elements_by_css_selector("tbody#standings-15151-content>tr")
        for rows in html:
            rtable = []
            cols = rows.find_elements_by_tag_name("td")
            for col in cols:
                rtable.append(col.text)
            curtable.append(rtable)
        return curtable
