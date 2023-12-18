from .models import StockQuote
from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime

def api_quote_data(request):
    
        api_url = "https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=hQZkTkAFBTc5zCybhElhf9lwcgxxoOHN"
        
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # return (data)
            
            objects_to_create = []
            for stock_data in data:
                quote = StockQuote(
                symbol=stock_data['symbol'],
                price=stock_data['price'],
                change_percentage=stock_data['changesPercentage'],
                change=stock_data['change'],
                day_low=stock_data['dayLow'],
                day_high=stock_data['dayHigh'],
                year_high=stock_data['yearHigh'],
                year_low=stock_data['yearLow'],
                market_cap=stock_data['marketCap'],
                price_avg_50=stock_data['priceAvg50'],
                price_avg_200=stock_data['priceAvg200'],
                volume=stock_data['volume'],
                avg_volume=stock_data['avgVolume'],
                open=stock_data['open'],
                previous_close=stock_data['previousClose'],
                earning_per_share=stock_data['eps'],
                price_to_earnings=stock_data['pe'],
                earnings_announcement=datetime.strptime(stock_data['earningsAnnouncement'], '%Y-%m-%dT%H:%M:%S.%f%z'), 
                shares_outstanding=stock_data['sharesOutstanding'],
                )
                objects_to_create.append(quote)
                
            StockQuote.objects.bulk_create(objects_to_create)
            print("data has been saved")
        else:
            return None