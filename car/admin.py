from django.contrib import admin
from advertisement.models import Advertisement
from car.models import Car

class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    extra = 0


class CarAdmin(admin.ModelAdmin):
    list_display = ('body', 'title', 'tip', 'color', 'model_year', 'description')
    list_filter = ('color', 'tip', 'model_year')
    inlines = [AdvertisementInline]


admin.site.register(Car, CarAdmin)