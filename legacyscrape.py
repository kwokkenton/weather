#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:53:17 2020
Legacy scrape

@author: kenton
"""

import urllib3
import bs4 as bs
#def scrapeWeatherold(year, month): 
#    ''' 
#    Year: 4 digit year value
#    Month: 2 digit month value
#    '''
##    year,month = str(year), str(month)
#    url = 'http://www.weather.gov.hk/wxinfo/pastwx/metob{0}{1}.htm'.format(year, month)
#    
#    labels =  []
#    data = []
#    
#    # Beautiful Soup request
#    req = urllib3.PoolManager()
#    res = req.request('GET', url)
#    soup = bs.BeautifulSoup(res.data, 'html.parser')
#
#    # Find first table on the page which is the daily weather data
#    table = soup.findAll("table")[0]
#    
#    # Parsing each row for data
#    rows = table.find_all('tr')
#    for row in rows:
#        item = row.find_all('td') # get table data values
#        rowlist = [] 
#        
#        for counter, value in enumerate(item):
#            if counter == 0:
#                rowlist.append(value.text) #ensure date is a string
#                
#            elif item: #remove null item values
#                try:
#                    float(value.text) #other data values are floats
#                    rowlist.append(float(value.text))
#                except:
#                    rowlist.append(0) #change null values to 0
#                
#            
#        if rowlist: #remove empty row values
#            data.append(rowlist)
#    
#    # Parsing the table for header
#    heading = table.find_all('th')  
#    for h in heading:
#        labels.append(str.strip(h.text))
#      
#    # modify spanned header     
#    labels[2: 3] = (i for i in labels[7:10])
#    labels = labels[0:9]
#    
#    #Rename first column
#    labels[0] = 'Date'
#    # Remove average rows
#    data = data[0:-3]
#
#    df = pd.DataFrame(data, columns = labels)
#    df['Date'] = year+ '/' + month+ '/'+ df['Date']
#    df['Date'] = pd.to_datetime(df['Date'])
#    return df

#def scrapeWeather(year, month): 
#    ''' 
#    Year: 4 digit year value
#    Month: 2 digit month value
#    '''
#    year,month = str(year), str(month)