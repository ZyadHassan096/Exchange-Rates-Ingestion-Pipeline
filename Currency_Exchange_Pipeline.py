# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:41:37 2022

@author: ROG
"""

import requests 
import pandas as pd
from datetime import date
import sys
import os
import csv

class my_dictionary(dict):
    def __init__(self): 
        self = dict()
        
    def add(self, key, value): 
        self[key] = value 



def get_Currency_Rate(base,required_countries):
    
    apiKey='https://v6.exchangerate-api.com/v6/b81be2b51bd91a878a0e92b0/latest/'
    response = requests.get(apiKey+base)
    data = response.json()
    exchangeRateAll = data['conversion_rates']
    
    exchangeRate = my_dictionary()
    
    for country in required_countries:
        exchangeRate.add(country, exchangeRateAll[country])
     
    return exchangeRate


def generat_target(data,filepath):
    
    columns = ["curncy","rate","Date"]
    todays_date = date.today()
    
    directory = str(todays_date.month)+ '_' + str(todays_date.year)+'/'
    parent_dir = filepath
    path = os.path.join(str(parent_dir), str(directory))
    file_name = 'ExchangeRate_' +str(todays_date.day)+'.csv'
    
    os.makedirs(path,exist_ok=True)
    finalRow= []
    with open(path+file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for Key in data:
            row =[]
            row.append(Key)
            row.append(str(data[Key]))
            row.append(todays_date)
            finalRow.append(row)
            writer.writerows(finalRow)
            finalRow= []
    
    


def main():
    
    base=sys.argv[1]
    required_countries=sys.argv[2].split(',')
    exchangeRate = get_Currency_Rate(base, required_countries)
    
    filepath = sys.argv[3]
    generat_target(exchangeRate,filepath)
    
if __name__ == "__main__":
    main()