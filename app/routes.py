from app import app
from flask import render_template
import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    #Set up Chrome options for Selenium Webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    #Initialize driver and use it to open CAEN Software Listings Page
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://caensoftware.engin.umich.edu/all')

    #Need to wait for page to fully render dynamic content
    time.sleep(1) 

    #Store the Page's HTML content
    html = driver.page_source
    
    #Convert to BeautifulSoup format
    soup = BeautifulSoup(html, 'lxml')

    #Find the desired Software Listings Table
    my_table = soup.find('table', {'id':'softwareListingTable'})

    #Find the Rows with the desired data 
    table_rows = my_table.find_all('tr')

    #Fill data entries by parsing the table
    Entries = []
    titles = ["Software Title", "Version", "Operating System", "Product Name", "Remote Access On-Campus", "Remote Access Off-Campus", "Restrictions"]
    Entries.append(titles)
    for tr in table_rows[1:]:
        tds = tr.find_all('td')
        Entry = []
        for td in tds:
            Entry.append(td.text.strip())
        Entries.append(Entry)

    
    return render_template('mytable.html', table=Entries)