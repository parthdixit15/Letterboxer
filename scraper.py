from requests_html import HTMLSession

import requests

import pandas as pd

from pandas import read_csv

from bs4 import BeautifulSoup

from random import randint

from time import sleep

import json


#reading the file 
data = read_csv("watchlist1.csv") 

#extracting the links column from the csv file and saving it in a list
links = data['Letterboxd URI'].tolist() 

#initialising an empty dictionary
streamings_available={} 

#starting a html session
session = HTMLSession() 

streamings_available={}

for link in links:
    #making a get request
    response = session.get(link)  

    #rendering the page with the link and making it sleep for 1 second incase the page is not rendered completely
    response.html.render(sleep = 1) 

    #parsing the page using beautiful soup
    soup= BeautifulSoup(response.html.html,'lxml') 

    #gettin the "services"
    services=soup.find_all('p',class_='service')  

    #getting the movie title
    name=soup.find('h1',class_='headline-1') 

    #initializing the movie with an empty list
    streamings_available.setdefault(name.text,[]) #initializing the movie with an empty list

    for service in services:

        service=service.find('desc')#getting service name

        if(service):

            streamings_available[name.text].append(service.text)

    #delaying the program so not to get rate limited
    sleep(randint(1,3))      

#creating a json file to store the list
with open(r'C:\Users\Asus\OneDrive\Desktop\reptile\letterboxer\streamings_available.json','w') as f:

    json.dump(streamings_available,f)      
