from django.contrib import admin
from advertisement.models import Advertisement
from car.models import Car




class CarAdmin(admin.ModelAdmin):
    list_display = ('body', 'title', 'tip', 'color', 'model_year', 'description')
    list_filter = ('color', 'tip', 'model_year')


admin.site.register(Car, CarAdmin)
