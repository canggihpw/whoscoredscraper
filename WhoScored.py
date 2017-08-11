# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:28:59 2017

@author: canggih
"""

from __future__ import division
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import WSTournamentList


class WhoScoredScraper:
    currURL = "https://www.whoscored.com/"

    def _openBrowser(self):
        try:
            #Load driver
            self._browser = webdriver.Chrome()
            #Load page
            self._browser.get(self.currURL)
            #Wait until certain element is visible
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
        
    def quitBrowser(self):
        self._browser.quit()

#    def getTournamentList(self):
#        #2-cols list. First col contains the name. Second col contains the url
#        self._tList = []
#        #Select list of tournaments
#        html = self._browser.find_elements_by_css_selector("ul#popular-tournaments-list>li")
#        for ht in html:
#            self._tList.append([ht.text,ht.find_element_by_tag_name("a").get_attribute("href")])
#        return self._tList
        
    def getCurrentTable(self,idTournament):
        curtable = []        
        self.currURL = WSTournamentList.TournamentLists[idTournament][1]
        self._openBrowser()

        html = self._browser.find_elements_by_css_selector("tbody#standings-15151-content>tr")
        for rows in html:
            rtable = []
            cols = rows.find_elements_by_tag_name("td")
            for col in cols:
                rtable.append(col.text)
            curtable.append(rtable)
        return curtable