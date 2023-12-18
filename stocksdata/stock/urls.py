from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
# from . import views

# router = DefaultRouter()
# router.register(r'stock-list', StockListViewSet)
# router.register(r'stock-profile', StockProfileViewSet)
# router.register(r'stock-quote', StockQuoteViewSet)

urlpatterns = [
    # path('data/', include(router.urls)),
    # path('data/search/', StockSearchView.as_view(), name='stock-list'),
    # path('quotedata/', views.api_quote_data, name='api_quote_data'),
    path('StockList/', StockListListView.as_view(), name='stock_list'),
    path('StockList/<str:pk>/', StockListRetrieveView.as_view(), name='stock_list_retrieve'),
    path('StockList/create/', StockListCreateView.as_view(), name='stock_list_create'),
    path('StockList/<str:pk>/update/', StockListUpdateView.as_view(), name='stock_list_update'),
    path('StockList/<str:pk>/delete/', StockListDestroyView.as_view(), name='stock_list_delete'),
    
    path('StockProfile/', StockProfileListView.as_view(), name='stock_profile'),
    path('StockProfile/<str:pk>/', StockProfileRetrieveView.as_view(), name='stock_profile_retrieve'),
    path('StockProfile/create/', StockProfileCreateView.as_view(), name='stock_profile_create'),
    path('StockProfile/<str:pk>/update/', StockProfileUpdateView.as_view(), name='stock_profile_update'),
    path('StockProfile/<str:pk>/delete/', StockProfileDestroyView.as_view(), name='stock_profile_delete'),
    
    path('StockQuote/', StockQuoteListView.as_view(), name='stock_quote'),
    path('StockQuote/<str:pk>/', StockQuoteRetrieveView.as_view(), name='stock_quote_retrieve'),
    path('StockQuote/create/', StockQuoteCreateView.as_view(), name='stock_quote_create'),
    path('StockQuote/<str:pk>/update/', StockQuoteUpdateView.as_view(), name='stock_quote_update'),
    path('StockQuote/<str:pk>/delete/', StockQuoteDestroyView.as_view(), name='stock_quote_delete'),
    
]


# urlpatterns = [
#     path('stock-list/', views.StockListViewSet.as_view(), name='stock-list'),
#     path('stock-profile/', views.StockProfileViewSet.as_view(), name='stock-profile'),
#     path('stock-quote/', views.StockQuoteViewSet.as_view(), name='stock-quote'),
# ]