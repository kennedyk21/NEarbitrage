# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 11:46:20 2020

@author: kenne
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

x=requests.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html')
y=BeautifulSoup(x.content,'html.parser')
b=(y.find(class_='2019coronavirus-summary'))
c=(b.find('ul').get_text())
print(c)