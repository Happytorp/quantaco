from django.contrib import admin
from .models import UserData

# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)

admin.site.register(UserData, UserDataAdmin)

