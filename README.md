# WhoScored Scraper

Python modules to scrap data from WhoScored by using Selenium.

## Requirements
* Python 2.7
* Selenium (https://pypi.python.org/pypi/selenium)

## Example
Import Browser and Tournament.
```
from PyWhoScored import Browser, Tournament
```
Get handler of web browser. Browsers used : 0 - Chrome, 1 - Firefox, 2 - Safari, 3 - Opera, 4 - Edge
```
handler = Browser.get_handler(0)
```
Using the handler, tournament data can be obtained. List of tournament id can be found in PyWhoScored/url-data/tournament.csv.
```
print Tournament.get_standings(handler,'1','2014/2015')
```
Quit web browser after obtaining the data.
```
Browser.quit_browser(handler)
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
