# -*- coding: utf-8 -*-
"""
Tournament.py

"""
from PyWhoScored import Browser
from PyWhoScored import _Common
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


# Get a list of standing of a tournament in particular season
def get_standings(handler,nationID,tournamentID,season):
    tList = _Common._extract_csv("PyWhoScored/url-data/allseasons.csv")
    for tL in tList:
        if (tL[0] == nationID) and (tL[1] == tournamentID) and (tL[2] == season):
            currURL = tL[3]

    Browser.open_browser(handler,currURL)
 
    # get unique ID of pages
    # whoscored use a unique number for each season
    unID = handler.find_elements_by_css_selector("head>link")[0]
    unID = unID.get_attribute("href").split("/")[10]
    
    # select the table
    html = handler.find_elements_by_css_selector("tbody#standings-"+unID+"-content>tr")
    curtable = []    
    for rows in html:
        rtable = []
        cols = rows.find_elements_by_tag_name("td")
        for col in cols:
            rtable.append(col.text)
        curtable.append(rtable)
    return curtable