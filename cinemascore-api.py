# cinemascore.py
# Licensed under the MIT License
# github: https://github.com/jhumms/Cinemascore-api
import requests
import re
from bs4 import BeautifulSoup
from base64 import b64encode
from lxml import html
import json
import string


def search(query):
    encodedQuery = b64encode(query.encode('ascii')).decode('utf-8')
    response = requests.get("https://api.cinemascore.com/guest/search/title/" + encodedQuery).text
    data = json.loads(response)
    print(data)
    
    
def all_movies():
    combo = list()
    letters = list(string.ascii_lowercase)
    for i in letters:
        for j in letters:
            combo.append(i+j)
    responses = ""
    for i in set(combo):        
        encodedQuery = b64encode(i.encode('ascii')).decode('utf-8')
        response = requests.get("https://api.cinemascore.com/guest/search/title/" + encodedQuery).text
    
        if responses == "":
            responses = response[0:len(response)-1]
        else:
            responses = responses + "," + response[1:len(response)-1]
       
    responses = responses + "]"
    data = json.loads(responses)
    print(list({v['TITLE']:v for v in data}.values()))
    
