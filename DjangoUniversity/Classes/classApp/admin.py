from django.contrib import admin

from .models import DjangoClasses # have to show where to find the class referenced below

# Django can construct a default form representation
admin.site.register(DjangoClasses)
