from django.contrib import admin
from advertisement.models import Advertisement
# from car.models import Car
#
#
# class CarInline(admin.TabularInline):
#     model = Car


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_urgent')
    list_filter = ('user',)
    # inlines = [CarInline]

admin.site.register(Advertisement, AdvertisementAdmin)
