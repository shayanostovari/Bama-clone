from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth import get_user_model

User = get_user_model()


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.set_password(obj.password)
    #     super().save_model(request, obj, form, change)