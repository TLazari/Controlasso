from django.contrib import admin
from .models import Account, Transfer, Stock, Trade, FavoriteStock

admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Stock)
admin.site.register(Trade)
admin.site.register(FavoriteStock)