#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup

def scrape(ticker_symbol):
    url = f"https://finance.yahoo.com/quote/{ticker_symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    
    data = {'ticker_symbol': ticker_symbol}
        

    data['previous_close'] = soup.find('table', {'class':'W(100%)'}).find_all('td')[1].text.strip() 
    data['open_value']= soup.find('table', {'class':'W(100%)'}).find_all('td')[3].text.strip() 
    data['bid']= soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip()
    data['ask']= soup.find('table', {'class':'W(100%)'}).find_all('td')[7].text.strip()
    data['days_range']= soup.find('table', {'class':'W(100%)'}).find_all('td')[9].text.strip()
    data['week_range']= soup.find('table', {'class':'W(100%)'}).find_all('td')[11].text.strip()
    data['volume']= soup.find('table', {'class':'W(100%)'}).find_all('td')[13].text.strip()
    data['avg_volume']= soup.find('table', {'class':'W(100%)'}).find_all('td')[5].text.strip()
    data['market_cap']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[1].text.strip() 
    data['beta']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[3].text.strip() 
    data['pe_ratio']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[5].text.strip()
    data['eps']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[7].text.strip() 
    data['earnings_date']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[9].text.strip()
    data['dividend_yield']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[11].text.strip() 
    data['ex_dividend_date']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[13].text.strip() 
    data['year_target_est']= soup.find('table', {'class':'W(100%) M(0) Bdcl(c)'}).find_all('td')[15].text.strip()
    return data


ticker_symbols = ['AMZN', 'TSLA', 'KO', 'GOOG', 'AAPL', 'DIS', 'FDX', 'LMT', 'CVS', 'K'] 
for symbol in ticker_symbols:
    stock = scrape(symbol)
    print(stock)
    
    
stock_data = [scrape(symbol) for symbol in ticker_symbols]

with open('stock_data.json', 'w', encoding = 'utf-8') as f:
    json.dump(stock_data, f)
    
CSV_FILE_PATH = 'stock_data.csv'
with open(CSV_FILE_PATH, 'w', newline = '', encoding = 'utf-8') as csvfile:
    fieldnames = stock_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(stock_data)
    
EXCEL_FILE_PATH = 'stock_data.xlsx'
df = pd.DataFrame(stock_data)
df.to_excel(EXCEL_FILE_PATH, index = False)

