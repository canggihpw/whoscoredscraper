# WhoScored Scraper

A simple python class to scrap data from WhoScored by using Selenium.

## Requirements
* Python 2.7
* Selenium (https://pypi.python.org/pypi/selenium)


## File descriptions
* WhoScored.py. A class file to be included

* WSTournamentList.py. A list containing tournament's id, name, and url

## Usage
Some major browsers: 0 - Chrome, 1 - Firefox, 2 - Safari, 3 - Opera, 4 - Edge

A complete list of <idTournament> is available in file WSTournamentList.py
```
from WhoScored import WhoScoredScraper

ws = WhoScoredScrapper(<browser used>)
print ws.get_current_table(<idTournament>)
ws.quit_browser()
```

## Current feature
* Retrieve the current standing of leagues

## Features to be added
* Match statistics
* Player statistics
* Past data
* and many more features

## License
GNU Affero General Public License v3.0
