#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup

def scrape_profile(ticker_symbol):
    url = f"https://finance.yahoo.com/quote/{ticker_symbol}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
        
    profile_data = {'ticker_symbol': ticker_symbol}

    profile_data['name'] = soup.find('h1', {'class':'D(ib) Fz(18px)'}).text.strip()
    profile_data['address'] = soup.find('p', {'class':'D(ib) W(47.727%) Pend(40px)'}).text.strip()
    profile_data['description'] = soup.find('p', {'class':'Fz(14px)'}).text.strip()  
    return profile_data


ticker_symbols = ['AMZN', 'TSLA', 'KO', 'GOOG', 'AAPL', 'DIS', 'FDX', 'LMT', 'CVS', 'K'] 
for symbol in ticker_symbols:
    profile = scrape_profile(symbol)
    print(profile)

    
stock_data = [scrape_profile(symbol) for symbol in ticker_symbols]

with open('Knickerbocker_stock_profile_data.json', 'w', encoding = 'utf-8') as f:
    json.dump(stock_data, f)
    
CSV_FILE_PATH = 'Knickerbocker_stock_profile_data.csv'
with open(CSV_FILE_PATH, 'w', newline = '', encoding = 'utf-8') as csvfile:
    fieldnames = stock_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(stock_data)
    
EXCEL_FILE_PATH = 'Knickerbocker_stock_profile_data.xlsx'
df = pd.DataFrame(stock_data)
df.to_excel(EXCEL_FILE_PATH, index = False)


# In[ ]:




