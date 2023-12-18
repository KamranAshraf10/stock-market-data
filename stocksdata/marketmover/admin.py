from django.contrib import admin
from .models import *

# Register your models here.

class PreMarketAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'company_name', 'table_reference' , '__str__')  # Add other fields as needed

admin.site.register(PreMarket, PreMarketAdmin)
# admin.site.register(PreMarket)
admin.site.register(CurrentMarket)

# class MarketDataAdmin(admin.ModelAdmin):
#     list_display = ('symbol', 'company_name', 'volume', 'change', 'percentage_change')
# admin.site.register(MarketData, MarketDataAdmin)

# class CurrentMarketAdmin(admin.ModelAdmin):
#     list_display = ('last', 'traded_at')
# admin.site.register(CurrentMarket, CurrentMarketAdmin)

# class PreMarketAdmin(admin.ModelAdmin):
#     list_display = ('price',)
# admin.site.register(PreMarket, PreMarketAdmin)
    
