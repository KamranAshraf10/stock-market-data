from django.contrib import admin
from .models import *

# Register your models here.
# class StockListAdmin(admin.ModelAdmin):
#     list_display = ('symbol', 'name', 'exchange', 'created_at', 'updated_at')  # Add 'created_at' and 'updated_at' here
    
# admin.site.register(StockList,StockListAdmin)


admin.site.register(StockList)
admin.site.register(StockQuote)
admin.site.register(StockProfile)

