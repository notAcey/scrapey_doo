# Simple Python Web Scraper
A web scraping tool developed in Python, designed to efficiently extract product listings from websites. This tool offers capabilities for swift sorting and filtering of the data, with added functionality to seamlessly export the information to Excel or CSV formats, facilitating enhanced data analysis, statistical evaluation, or just personal enjoyment.

## Currently Supported Websites
* [PC Garage](https://www.pcgarage.ro/ "pcgarage.ro") - scraped with [Selenium](https://pypi.org/project/selenium/)
* [Altex](https://altex.ro/ "altex.ro") - scraped with [Selenium](https://pypi.org/project/selenium/)
* [OLX](https://www.olx.ro/ "olx.ro") - scraped with [Requests](https://pypi.org/project/requests/)

## Used Technologies
* [Requests](https://pypi.org/project/requests/) and [Selenium's WebDriver](https://pypi.org/project/selenium/) for retrieving the website's HTML
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) for parsing the retrieved HTML
* [Pandas](https://pypi.org/project/pandas/) and [openpyxl](https://pypi.org/project/openpyxl/) for quick data manipulation and export
* [Flask](https://pypi.org/project/Flask/) for integrating the scraper into a WebApp
* [Bootstrap](https://getbootstrap.com) (before we transition to React) to make it a little more eye-catching

## Running the App
* [Python 3](https://www.python.org/downloads/) is required to run the app.
* After opening the project in your preffered IDE, you will have to run the next commands:
```bash
  pip install requests
```
```bash
  pip install selenium
```
```bash
  pip install pandas
```
```bash
  pip install bs4
```
```bash
  pip install openpyxl
```
```bash
  pip install flask
``` 
```bash
  npm i -g @structure-codes/cli # Optional(if you want to see the structure of the project in a .tree file)
```
* Run the 'app.py' file: ```bash python app.py ``` in the terminal of the IDE (Visual Studio Code) or any other terminal and paste the http link of the [**supported website**](#currently-supported-websites) you want to scrape.
* For **VSCode users** only, make sure to go into IDE Settings (Ctrl+,) and search for "Pylance path add'. Under "Python › Analysis: Include", click on "Add Item", then enter the path of the folder in which the project is located (ex: "A:\Projects\scrapey-doo"

## How to use?
* Once you execute the app.py script, hold Ctrl and right-click the link next to "Running on". This action will automatically launch the link in your default web browser.
* Upon opening, you'll encounter a textbox where you can input the desired link, accompanied by various buttons to perform operations on the scraped data.
* After the scraping process completes, the data will be displayed, allowing you to conduct various operations on it.
