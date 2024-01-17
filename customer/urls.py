from django.urls import path, include
from .views import CreateCustomer, ListCustomer, update_customer, delete_customer

urlpatterns = [
    path('createCustomer', CreateCustomer.as_view()),
    path('listCustomer', ListCustomer.as_view()),
    path('updateCustomer/<int:pk>', update_customer),
    path('deleteCustomer/<int:pk>', delete_customer),
]