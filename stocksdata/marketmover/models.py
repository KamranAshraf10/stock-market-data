from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class MarketData(models.Model):
    symbol = models.CharField(max_length=20, null=True)
    company_name = models.CharField(max_length=50, null=True)
    volume = models.CharField(max_length=50,null=True)
    change = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    percentage_change = models.FloatField(null=True)
    table_reference = models.CharField(max_length=20, null=True)
    
    
    class Meta:
        abstract=True
    
class CurrentMarket(MarketData):
    last = models.DecimalField(max_digits=10, decimal_places=2)
    traded_at = models.DateTimeField()
    
class PreMarket(MarketData):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Symbol: {self.symbol}"
