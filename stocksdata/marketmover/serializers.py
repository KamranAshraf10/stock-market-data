from dataclasses import fields
from rest_framework import serializers
from .models import *

class CurrentMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMarket
        fields = '__all__'
        
class PreMarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreMarket
        fields = '__all__'
        # fields = ['symbol', 'company_name', 'volume', 'change', 'percentage_change', 'table_reference', 'price']