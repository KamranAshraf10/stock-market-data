from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


# These are model Viewsets
# class StockListViewSet(viewsets.ModelViewSet):
#     queryset = StockList.objects.all()
#     serializer_class = StockListSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['symbol']
    
# class StockSearchView(APIView):
#     def get(self, request):
#         symbol = request.query_params.get('search', None)
#         if symbol:
#             stocks = StockList.objects.filter(symbol=symbol)
#             serializer = StockListSerializer(stocks, many=True)
#             return Response(serializer.data)
#         return Response("Please provide a search parameter.", status=status.HTTP_400_BAD_REQUEST)

class StockListListView(ListAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer
    
class StockListRetrieveView(RetrieveAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer
    
class StockListCreateView(CreateAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer
    
class StockListUpdateView(UpdateAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer
    
class StockListDestroyView(DestroyAPIView):
    queryset = StockList.objects.all()
    serializer_class = StockListSerializer

# These are model Viewsets
# class StockProfileViewSet(viewsets.ModelViewSet):
#     queryset = StockProfile.objects.all()
#     serializer_class = StockProfileSerializer

class StockProfileListView(ListAPIView):
    queryset = StockProfile.objects.all()
    serializer_class = StockProfileSerializer

class StockProfileRetrieveView(RetrieveAPIView):
    queryset = StockProfile.objects.all()
    serializer_class = StockProfileSerializer
    
class StockProfileCreateView(CreateAPIView):
    queryset = StockProfile.objects.all()
    serializer_class = StockProfileSerializer
    
class StockProfileUpdateView(UpdateAPIView):
    queryset = StockProfile.objects.all()
    serializer_class = StockProfileSerializer
    
class StockProfileDestroyView(DestroyAPIView):
    queryset = StockProfile.objects.all()
    serializer_class = StockProfileSerializer
    
# These are model Viewsets
# class StockQuoteViewSet(viewsets.ModelViewSet):
#     queryset = StockQuote.objects.all()
#     serializer_class = StockQuoteSerializer

class StockQuoteListView(ListAPIView):
    queryset = StockQuote.objects.all()
    serializer_class = StockQuoteSerializer
    
class StockQuoteRetrieveView(RetrieveAPIView):
    queryset = StockQuote.objects.all()
    serializer_class = StockQuoteSerializer
    
class StockQuoteCreateView(CreateAPIView):
    queryset = StockQuote.objects.all()
    serializer_class = StockQuoteSerializer

class StockQuoteUpdateView(UpdateAPIView):
    queryset = StockQuote.objects.all()
    serializer_class = StockQuoteSerializer
    
class StockQuoteDestroyView(DestroyAPIView):
    queryset = StockQuote.objects.all()
    serializer_class = StockQuoteSerializer



# These are general Views
# def api_quote_data(request):
#     try:
#         api_url = "https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=hQZkTkAFBTc5zCybhElhf9lwcgxxoOHN"
        
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             response_data = {"data": data}
#             return JsonResponse(response_data)
#         else:
#             return JsonResponse({"error": "Failed to retrieve data from the API"}, status=500, safe=False)
        
#     except Exception as e:
#         return JsonResponse({"error": str(e)})
    
# def api_stock_data(request):
#     try:
#         api_url = "https://financialmodelingprep.com/api/v3/available-traded/list?apikey=hQZkTkAFBTc5zCybhElhf9lwcgxxoOHN"
        
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             data = response.json()
#             response_data = {"data": data}
#             return JsonResponse(response_data)
#         else:
#             return JsonResponse({"error": "Failed to retrieve data from the API"}, status=500, safe=False)
        
#     except Exception as e:
#         return JsonResponse({"error": str(e)})
