from django.contrib import admin

# registsering the models
from .models import Account, Transaction

admin.site.register(Account)

admin.site.register(Transaction)
