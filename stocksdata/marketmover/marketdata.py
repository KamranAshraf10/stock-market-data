from pydoc import stripid
from bs4 import BeautifulSoup
from . models import PreMarket
from .models import *
from django.shortcuts import render
import requests



def scrap_pre_market():
    
    url = "https://www.marketwatch.com/tools/screener/premarket"
    data = requests.get(url)
    
    soup = BeautifulSoup(data.text,'html.parser')
    
    
    all_tables = soup.find_all('table')
    # for table in all_tables:
        
    if all_tables:  # Ensure at least one table exists
        
        first_table = all_tables[0]  # Accessing the first table in the result set
        # print("LEADERS")
        for row in first_table.find_all('tr')[1:]:
            cells = row.find_all(['th', 'td'])
            cell_data1 = [cell.get_text(strip=True) for cell in cells]
            
            new_data1 = PreMarket(
                table_reference='LEADERS',
                symbol=cell_data1[0],
                company_name=cell_data1[1],
                price =cell_data1[2].replace('$', ''),
                volume=cell_data1[3],
                change=cell_data1[4].replace('%', ''),
                percentage_change=cell_data1[5].rstrip('%'),
            )
            new_data1.save()
            # print(new_data1.symbol)
           
            print(" ")

        second_table = all_tables[1]  # Accessing the 2nd table in the result set
        # print("LAGGARDS")  
        for row in second_table.find_all('tr')[1:]:
            cells = row.find_all(['th', 'td'])
            cell_data2 = [cell.get_text(strip=True) for cell in cells]
            # print(cell_data2)
            
            new_data2 = PreMarket(
                table_reference='LAGGARDS',
                symbol=cell_data2[0],
                company_name=cell_data2[1],
                price = cell_data2[2].replace('$', ''),
                volume=cell_data2[3],
                change=cell_data2[4].replace('-', '-'),
                percentage_change= cell_data2[5].replace('%', ''),
            )
            new_data2.save()
        
        # print(" ")   
            
        third_table = all_tables[1]  # Accessing the 3rd table in the result set
        # print("MOST ACTIVE")  
        for row in third_table.find_all('tr')[1:]:
            cells = row.find_all(['th', 'td'])
            cell_data3 = [cell.get_text(strip=True) for cell in cells]
            # print(cell_data3)
            
            new_data3 = PreMarket(
                table_reference='MOST ACTIVE',
                symbol=cell_data3[0],
                company_name=cell_data3[1],
                price = cell_data3[2].replace('$', ''),
                volume=cell_data3[3],
                change=cell_data3[4].replace('-', '-'),
                percentage_change=cell_data3[5].rstrip('%'),
                
            )
            new_data3.save()        
        # print(" ")     
    
scrap_pre_market()
# print(scrap_pre_market())