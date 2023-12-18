from django.db import models
from django.forms import CharField
from flask import request
from django.utils import timezone

# Create your models here.
class StockList(models.Model):
    symbol = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50, null=True)
    exchange = models.CharField(max_length=50,null=True)
    exchange_short_name = models.CharField(max_length=20,null=True)
    stock_type = models.CharField(max_length=20,null=True)
    
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
    
class StockQuote(models.Model):
    symbol = models.CharField(max_length=20, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    change_percentage = models.FloatField()
    change = models.DecimalField(max_digits=10, decimal_places=2)
    day_low = models.DecimalField(max_digits=10, decimal_places=2)
    day_high = models.DecimalField(max_digits=10, decimal_places=2)
    year_high = models.DecimalField(max_digits=10, decimal_places=2)
    year_low = models.DecimalField(max_digits=10, decimal_places=2)
    market_cap = models.BigIntegerField()
    price_avg_50 = models.DecimalField(max_digits=10, decimal_places=2)
    price_avg_200 = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()
    avg_volume = models.BigIntegerField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    previous_close = models.DecimalField(max_digits=10, decimal_places=2)
    earning_per_share = models.FloatField()
    price_to_earnings = models.FloatField()
    earnings_announcement = models.DateTimeField()
    shares_outstanding = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # created and updated


class StockProfile(models.Model):
    symbol = models.CharField(max_length=20, primary_key=True)
    beta = models.FloatField()
    last_div = models.FloatField()
    stock_range = models.CharField(max_length=50)
    currency = models.CharField(max_length=10)
    cik = models.CharField(max_length=20)
    isin = models.CharField(max_length=20)
    cusip = models.CharField(max_length=20)
    industry = models.CharField(max_length=50)
    website  = models.URLField(max_length=200)
    description = models.TextField()
    ceo = models.CharField(max_length=50)
    sector = models.CharField(max_length=50) 
    country = models.CharField(max_length=50) 
    full_time_employees = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=10)
    dcf_diff = models.FloatField()
    dcf = models.FloatField()
    image = models.URLField(max_length=200)
    ipo_date = models.DateField()
    default_image = models.BooleanField(default=False)
    is_etf = models.BooleanField(default=False)
    is_actively_trading = models.BooleanField(default=True)
    is_adr = models.BooleanField(default=False)
    is_fund = models.BooleanField(default=False)
    