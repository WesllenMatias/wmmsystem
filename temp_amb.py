import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

def get_temp():
    uri = "http://10.0.0.195/"
    options = Options()
    options.headless = True
    get_url = webdriver.Firefox(options=options)
    get_url.get(uri)
    sleep(10)
    page = get_url.page_source
    bs = BeautifulSoup(page,'html.parser')
    temp = bs.find("span",{"id":"TemperatureValue"})
    humid = bs.find("span",{"id":"HumidityValue"})
    print(temp.text, humid.text)
    get_url.quit()


get_temp()