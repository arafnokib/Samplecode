import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from csvconvert import csv_converter
from scraper import scraper
import pandas as pd

#Both variables to be inputted as function parameters

driver = '/Users/arafnokib/Downloads/Whitehat/Python/WebScraping/web4/chromedriver'


#calling class, setting data as a variable which is running the function in a class, calling the function to convert data to csv
scraper = scraper();
url = "https://animeseries.so/search/character="

data = scraper.anime_scrape(url, driver)

d1 = pd.DataFrame({
    'name' : data[0],
    'descriptions' : data[2],
    'status': data[3],
    'release_year' : data[6],
    'genres' : data[4],
    'slug': data[5],
    'image_url': data[1],
    'total_episodes': data[7],
    'episode_links': data[8],
    'episode_i_frame_array': data[9],
})

d1.to_csv('sample.csv')
#csvmaker = csv_converter()
#csvmaker.anime_convertcsv(data[0], data[1], data[2])

