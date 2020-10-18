# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:21:36 2020

@author: Shoaib
"""
import glassdoor_scrapper as gs
import pandas as pd
path = "C:/Users/Shoaib/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data_scientist', 1000, False, path, 15)

df.to_csv("ds_salary_proj_copy.csv")

