from django.contrib import admin
from .models import *

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ['Hotel_name','Hotel_price','Hotel_description']


admin.site.register(amenities)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(HotelImage)
