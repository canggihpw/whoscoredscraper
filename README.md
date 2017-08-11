# WhoScored Scraper

A simple python class to scrap data from WhoScored by using Selenium.

## Requirements
* Python 2.7
* Selenium (https://pypi.python.org/pypi/selenium)

## File descriptions
* WhoScored.py. A class file to be included

* WSTournamentList.py. A list containing tournament's id, name, and url

## How to use
A complete list of tournament id is available in WSTournamentList.py
```
from WhoScored import WhoScoredScrapper

ws = WhoScoredScrapper()
idTournament = 0
print ws.getCurrentTable(idTournament)
ws.quitBrowser()
```

## Current feature
* Retrieve the current standing of leagues

## Features to be added
* Match statistics
* Player statistics
* Past data
* and many more features
