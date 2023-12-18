from rest_framework import serializers
from .models import StockList, StockProfile, StockQuote

class StockListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockList
        fields = '__all__'
        
class StockProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProfile
        fields = '__all__'

class StockQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockQuote
        fields = '__all__'