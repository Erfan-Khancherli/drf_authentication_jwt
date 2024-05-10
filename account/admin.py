from django.contrib import admin
from account.models import CustomUser
# from rest_framework.authtoken.models import Token

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email'  ,'first_name' , 'last_name' ,'password']


admin.site.register(CustomUser, CustomUserAdmin)

# class FilterTokenAdmin(admin.ModelAdmin):
#     search_fields = ['user__email','user__username']

# admin.site.register(Token,FilterTokenAdmin)