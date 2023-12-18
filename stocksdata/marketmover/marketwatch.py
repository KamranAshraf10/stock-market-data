import requests
from bs4 import BeautifulSoup
import pandas as pd

class market:
    open = "N/A"
    day_range = "N/A"
    week52range = "N/A"
    market_cap= "N/A"
    shares_outstanding = "N/A"
    public_float= "N/A"
    beta = "N/A"
    rev_per_employee = "N/A"
    eps = "N/A"
    p_e_ratio = "N/A"
    stock_yield = "N/A"
    dividend = "N/A"
    ex_dividend_date = "N/A"
    short_interest = "N/A"
    percent_of_float_shorted = "N/A"
    average_volume = "N/A"
    
    def __init__(self, ticker):
        self.ticker=ticker
        market_response=self.scrape_market_watch(ticker) 
        print("ali")
        # print(market_response)
        # self.scrape_market_watch()
        self.open=market_response['open']
        self.day_range=market_response['day_range']
        self.week52range=market_response['52_week_range']
        self.market_cap=market_response['market_cap']
        self.shares_outstanding=market_response['shares_outstanding']
        self.public_float=market_response['public_float']
        self.rev_per_employee=market_response['rev._per_employee']
        self.eps=market_response['eps']
        self.p_e_ratio=market_response['p/e_ratio']
        self.stock_yield=market_response['yield']
        self.dividend=market_response['dividend']
        self.ex_dividend_date=market_response['ex-dividend_date']
        self.short_interest=market_response['short_interest']
        self.percent_of_float_shorted=market_response['%_of_float_shorted']
        self.average_volume =market_response['average_volume']

        
    def scrape_market_watch(self, ticker):
        market_response=dict ()
        url = "https://www.marketwatch.com/investing/stock/"+ticker+"?mod=search_symbol"
        data = requests.get(url).content
        soup = BeautifulSoup(data,'html.parser')
        list_all = soup.find('ul',class_="list list--kv list--col50")
        # print(list_all)
        
        if list_all:
            cells = list_all.find_all('li', class_="kv__item")  # Find all list items with class 'kv__item'
            # print(cells)
            for item in cells:
                label = item.find('small', class_="label").text.strip().replace(" " , "_").lower()  # Find the label within each list item
                value = item.find('span',class_="primary").text.strip()
                market_response[label] = value
                # print(f" : {label}, : {value}")
                
                # market_response[label] = value
                # market_response['open']= open
                # market_response['day_range']= day_range
                # market_response['week52range']= week52range
                # market_response['market_cap']= market_cap
                # market_response['shares_outstanding']= shares_outstanding
                # market_response['public_float']= public_float
                # market_response['rev_per_employee']= rev_per_employee
                # market_response['eps']= eps
                # market_response['p_e_ratio']= p_e_ratio
                # market_response['stock_yield']= stock_yield
                # market_response['dividend']= dividend
                # market_response['ex_dividend_date']= ex_dividend_date
                # market_response['short_interest']= short_interest
                # market_response['stock_yield']= stock_yield
                # market_response['percent_of_float_shorted']= percent_of_float_shorted 
                # market_response['average_volume']= average_volume

        return market_response
    

print(vars(market('AAPL')))
# P.scrape_market_watch('AAPL')

