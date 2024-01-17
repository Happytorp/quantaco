from django.contrib import admin
from customer.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'phone_number')

admin.site.register(Customer, CustomerAdmin)

