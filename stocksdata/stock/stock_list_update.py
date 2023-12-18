from .models import StockList
from django.shortcuts import render
import requests

def api_stock_data():
    api_url = "https://financialmodelingprep.com/api/v3/available-traded/list?apikey=hQZkTkAFBTc5zCybhElhf9lwcgxxoOHN"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
    
        objects_to_create = []
        for stock_data in data:
            stock = StockList(
                symbol=stock_data['symbol'],
                name=stock_data['name'],
                exchange=stock_data['exchange'],
                exchange_short_name=stock_data['exchangeShortName'],
                stock_type=stock_data['type']
            )
            objects_to_create.append(stock)

        StockList.objects.bulk_create(objects_to_create)
        print("Data has been saved")
    else:
        return None
 
    
    # objects_to_update = []
    # for updated_stock_data in data:
    #     stock_instance = StockList.objects.get(symbol=updated_stock_data['symbol'])
    #     # Update instance attributes
    #     stock_instance.name = updated_stock_data['name']
    #     stock_instance.exchange = updated_stock_data['exchange']
    #     stock_instance.exchange_short_name = updated_stock_data['exchangeShortName']
    #     stock_instance.stock_type = updated_stock_data['type']
    #     objects_to_update.append(stock_instance)

    #     # Bulk update
    #     StockList.objects.bulk_update(objects_to_update, ['name', 'exchange', 'exchange_short_name', 'stock_type'])
    #     print("Data has been updated in bulk")


        # return (data)
    #     for stock_data in data:
    #         StockList.objects.create(
    #         symbol=stock_data['symbol'],
    #         name=stock_data['name'],
    #         exchange=stock_data['exchange'],
    #         exchange_short_name=stock_data['exchangeShortName'],
    #         stock_type=stock_data['type']
    #         ).save()
    #         print("data has been saved")
    #         break 
    # else:
    #     return None
    
        # if data:
        #     print(stock_data['symbol'])
        #     stock_list_instances = [
        #         StockList(
        #             symbol=stock_data['symbol'],
        #             name=stock_data['name'],
        #             exchange=stock_data['exchange'],
        #             exchange_short_name=stock_data['exchangeShortName'],
        #             stock_type=stock_data['type']
        #         )
        #         for stock_data in data
        #     ]
        #     StockList.objects.bulk_create(stock_list_instances)
        
