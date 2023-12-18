from .models import StockProfile
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd


def api_profile_data():
    
        api_url = "https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=edoExRERYzYGHygq9rIMWFFQPmnRJw2M"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            # return (data)
            objects_to_create = []
            for stock_data in data:
                profile = StockProfile(
                    symbol=stock_data['symbol'],
                    beta=stock_data['beta'],
                    last_div=stock_data['lastDiv'],
                    stock_range=stock_data['range'],
                    currency=stock_data['currency'],
                    cik=stock_data['cik'],
                    isin=stock_data['isin'],
                    cusip=stock_data['cusip'],
                    industry=stock_data['industry'],
                    website=stock_data['website'],
                    description=stock_data['description'],
                    ceo=stock_data['ceo'],
                    sector=stock_data['sector'],
                    country=stock_data['country'],
                    full_time_employees=stock_data['fullTimeEmployees'],
                    phone=stock_data['phone'],
                    address=stock_data['address'],
                    city=stock_data['city'],
                    state=stock_data['state'],
                    zip=stock_data['zip'],
                    dcf_diff=stock_data['dcfDiff'],
                    dcf=stock_data['dcf'],
                    image=stock_data['image'],
                    ipo_date=stock_data['ipoDate'],
                    default_image=stock_data['defaultImage'],
                    is_etf=stock_data['isEtf'],
                    is_actively_trading=stock_data['isActivelyTrading'],
                    is_adr=stock_data['isAdr'],
                    is_fund=stock_data['isFund']
                )
                objects_to_create.append(profile)
                
            StockProfile.objects.bulk_create(objects_to_create)
            print("data has been saved")
        else:
            return None