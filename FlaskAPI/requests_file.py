# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:03:55 2020

@author: Shoaib
"""
import requests
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL, headers=headers, json=data)

r.json()