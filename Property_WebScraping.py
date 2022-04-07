# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:08:26 2022

@author: Purvarth
"""

from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
#import re

#variables
houselinks = []
housenames = []
housename = []
houselinks2 = []
housenames2 = []
houseBHK= []
availability = []
housesize = []
houseprice = []
houseaddress = []
housedesc = []
#houseaddress2 = []
#housedesc2 = []
office_address = []
propertydesc = []


#city name
city = "thane"

for num in range(1,50):
    link = "https://www.commonfloor.com/"+ city +"-property/projects?page=" + str(num)
    #print(link)

    #Beautiful Soup
    scrp = requests.get(link)
    soup = BeautifulSoup(scrp.content, "html5lib")

    #Flat name
    names = soup.find_all(class_="snb-projecttile-ab")

    #Flat link
    links = soup.find_all('a',attrs = {"class" : "snb-projecttile-ab"}, href=True)



    for name in names:
        #print(name.h2.text.strip())
        housenames.append(name.h2.text.strip())
        #print(name.a["href"].strip())
    
    for link in links:
        #print("https://www.commonfloor.com" + link['href'])
        templink = "https://www.commonfloor.com" + link['href']
        houselinks.append(templink)
    
    '''#test
    for m in range(len(houselink)):
        print(houselink)'''
        
for houselink,housename in zip(houselinks,housenames):
    #Beautiful Soup
    scrp = requests.get(houselink)
    soup = BeautifulSoup(scrp.content, "html5lib")
    
    #Office address
    officeaddress = soup.find_all(class_="contenttext mrtp10")
    
    #Flat Address
    Flataddress = soup.find_all(class_="_pro_title")
    
    #Flat Desc
    Flatdesc = soup.find_all('div',attrs = {"id" : "about"})

    #Builder description
    desc = soup.find_all(class_="col-xs-12 col-sm-12")
    

    names = soup.find_all(class_="body")
    lands = soup.find_all(class_="smtext")
    
    '''#for land in lands:
    #print(land.text.strip())
    for i in address:
        #print(i.text.strip())
        houseaddress.append(i.text.strip())
    
    for descs in desc:
        #print(descs.div.div.text.strip())
        housedesc.append(descs.div.text.strip())'''
    
    for name in names:
        #print(name.span.text.strip())
        houseBHK.append(name.span.text.strip())
        
        #print(houselink)
        houselinks2.append(houselink)
        
        housenames2.append(housename)
        
        #print(name.small.text.strip())
        availability.append(name.small.text.strip())
        
        #print(name.findAll('div')[2].text.strip())
        housesize.append(name.findAll('div')[2].text.strip())
        
        #print(name.findAll('div')[3].text.strip())
        houseprice.append(name.findAll('div')[3].text.strip())
       
        
        #for land in lands:
        #print(land.text.strip())
        for i in officeaddress:
            try:
                #print(i.text.strip())
                office_address.append(i.text.strip())
            except:
                office_address.append("-")
                
        for i in Flataddress:
            try:    
                tempaddress = housename +", "+ i.findAll('a')[1].text.strip() +", "+ city
                houseaddress.append(tempaddress) 
            except:
                houseaddress.append("-")
                
        for i in Flatdesc:
            try:
                propertydesc.append(i.findAll('p')[0].text.strip())
            except:
                propertydesc.append("-")
                
        for descs in desc:
            try:
                #print(descs.div.div.text.strip())
                housedesc.append(descs.div.text.strip())
            except:
                housedesc.append('-')
                
        if(len(housenames2) != len(propertydesc)):
            for i in range( len(housenames2) - len(propertydesc) ):
                propertydesc.append('-')
 
        if(len(housenames2) != len(housedesc)):
            for i in range( len(housenames2) - len(housedesc) ):
                housedesc.append('-')
                
        if(len(housenames2) != len(office_address)):
            for i in range( len(housenames2) - len(office_address) ):
               office_address.append('-')
               
        if(len(housenames2) != len(houseaddress)):
            for i in range( len(housenames2) - len(houseaddress) ):
                houseaddress.append('-')
        
#Excel  
Property_details = pd.DataFrame()

Property_details["Property_name"] = housenames2 
Property_details["Property Address"] = houseaddress
Property_details["Property_BHK"] = houseBHK
Property_details["Availability"] = availability
Property_details["Property_size"] = housesize
Property_details["Property_price"] = houseprice  
Property_details["Property_Description"] = propertydesc
Property_details["Builder Description"] = housedesc
Property_details["Office address"] = office_address
Property_details["Link"] = houselinks2  


Property_details.to_csv("Property_"+city+".csv", encoding = "utf-8")