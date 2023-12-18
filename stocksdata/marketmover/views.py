from django.shortcuts import render
import requests
from django.http import JsonResponse
from . models import *
from . serializers import *
from rest_framework import viewsets


# Create your views here.


# These are model Viewsets
class PreMarketViewSet(viewsets.ModelViewSet):
    queryset = PreMarket.objects.all()
    serializer_class = PreMarketSerializer
    
    
# def scrap_data(request):
#     try:
#         api_url = "https://www.marketwatch.com/tools/screener/premarket"
        
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             return JsonResponse(data)
#         else:
#             return JsonResponse({"error": "Failed to retrieve data from the API"}, status=500)
        
#     except Exception as e:
#         return JsonResponse({"error": str(e)})