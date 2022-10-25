# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:02:28 2022

@author: PPK
"""
import pandas as pd

### Calculate VaR from historical data in the file provided
### Input: File name (string), Output: VaR (float)

### The following function calculates VaR, given the filename
def Calculate_VaR (p):
    stockprice = pd.read_csv(p) 
    stockprice = stockprice.replace(',','', regex=True)   
    stockprice['MeanPrice']=stockprice.apply(lambda x : (float(x['High Price']) + float(x['Low Price']))/2, axis=1)
    stockprice['Return']=stockprice['MeanPrice'].diff()
    stockprice = stockprice.dropna(subset=['Return'])
    VaR = stockprice['Return'].quantile(q=0.95)             # Change q based on approporiate confidence level
    print(stockprice)
    print (VaR)       
    return VaR

filename = ''           
stockwiseVaRs = []
VaR = 0
### The user can enter the name of the file containing the stock prices to be used for VaR calculation
while True:
    print('Enter file name along with extension:')
    filename = input()          # Should contain full path with extension
    if filename == "End":
        break
    VaR = Calculate_VaR (filename)
    stockwiseVaRs.append({filename : VaR})
print (stockwiseVaRs)
