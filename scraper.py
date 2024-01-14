from requests_html import HTMLSession

import requests

import pandas as pd

from pandas import read_csv

from bs4 import BeautifulSoup

from random import randint

from time import sleep

import json



data = read_csv("watchlist1.csv")

links = data['Letterboxd URI'].tolist()

streamings_available={}

session = HTMLSession()

streamings_available={}

for link in links:

    response = session.get(link)

    response.html.render(sleep = 1)

    soup= BeautifulSoup(response.html.html,'lxml')

    services=soup.find_all('p',class_='service')

    name=soup.find('h1',class_='headline-1')

    streamings_available.setdefault(name.text,[])

    for service in services:

        service=service.find('desc')

        if(service):

            streamings_available[name.text].append(service.text)

    sleep(randint(1,3))      

with open(r'C:\Users\Asus\OneDrive\Desktop\reptile\letterboxer\streamings_available.json','w') as f:

    json.dump(streamings_available,f)      
