from django.contrib import admin
from advertisement.models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_urgent', 'get_car_details')
    list_filter = ('user',)

    def get_car_details(self, obj):
        car_details = f"{obj.car.model_year} ({obj.car.title}) - {obj.car.tip}, Color: {obj.car.color}"
        return car_details

    get_car_details.short_description = 'Car Model'

    def get_readonly_fields(self, request, obj=None):
        return ['car_details']

    def car_details(self, obj):
        if obj.car:
            return (f"ID : {obj.car.id} \n Car : {obj.car.title} \n Color : ({obj.car.color}) \n"
                    f" Tip : {obj.car.tip}, \n Model year : {obj.car.model_year} \n Body {obj.car.body} \n"
                    f" Description : {obj.car.description} \n ")
        return "No Car"

    car_details.short_description = 'Car Details'

    fieldsets = ((None, {'fields': ('title', 'user', 'is_urgent', 'car_details')}),)


admin.site.register(Advertisement, AdvertisementAdmin)
