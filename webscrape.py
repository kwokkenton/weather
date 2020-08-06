#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uses selenium to scrape weather data from HKO
because it uses dynamic HTML

@author: kenton
"""

#Web scraping

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

PATH = '/Users/kenton/Documents/chromedriver'

class weatherTable:
    def __init__(self, year, month):
        self.year = str(year)
        self.month = str(month)
        
        chrome_options = Options()  
        chrome_options.add_argument("--headless") #headless means the browser won't pop up
        url = "https://www.hko.gov.hk/en/cis/dailyExtract.htm?y={0}&m={1}".format(self.year, self.month)
        
        driver = webdriver.Chrome(PATH, options=chrome_options)
        driver.implicitly_wait(5)
        driver.get(url)

        self.driver = driver
        pass
    
    
    def get_column_info(self):
        # important to use find_elements instead of element to get a list 
        # looking for all th elements with specific header class
        columns = ([i.text for i in self.driver.
                        find_elements_by_xpath('//th[@class = "td_normal_class"]')])
#        self.driver.quit()
        
        ### cleaning
        columns.remove('Hong Kong Observatory') 
        
        try:  #this version includes the wind speed (extra columns)
            ### modify spanned header
            #remove measurement station names
            columns.remove("King's Park") 
            columns.remove('Waglan Island^')
            
            #fix multiindex for temperature
            columns[2: 3] = (i for i in columns[10:13])
            
        except ValueError:  #this is the version without the wind speed
            #fix multiindex for temperature
            columns[2: 3] = (i for i in columns[7:10])
        
        columns = columns[:-3] #remove now duplicated columns
        
        return columns
    
    
    def clean_elem(self, element):
        element = element.replace('Trace', '0.05')
        element = element.replace('#', '')
        try:
            element = float(element)
        except:
            pass
        return element
    
    
    def get_data(self): 
        
        rows = ([i.text for i in self.driver.
                        find_elements_by_xpath('//tr [contains(@class, th)]')])
#        self.driver.quit()
        
        ### turn extraction into array
        for ridx,r in enumerate(rows): #split string of numbers into list
            rows[ridx] = r.split()
            
            for eidx, element in enumerate(rows[ridx]): #turn list of strings into floats
                if eidx != 0: #don't change first element (date) intp float
                    rows[ridx][eidx] = self.clean_elem(element)
        return rows
    
    
    def get_df(self):
        columns = self.get_column_info()
        rows = self.get_data()
        
        x = pd.DataFrame(rows, columns= columns)
        
        # remove mean data (last two rows)
        return x.iloc[:-2,:]
    
    
    def modify_datetime(self, df):
        df['Day'] = df['Day'].astype(str)
        df['Day'] = self.year + '/' + self.month +'/' + df['Day']     
        df['Day'] = pd.to_datetime(df['Day'])
        return df


t = weatherTable(year = 2020, month=6)
df = t.get_df()
df = t.modify_datetime(df)
