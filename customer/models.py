from django.db import models

# Create your models here.
from user.models import UserData

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(TimeStampMixin):
    user = models.ForeignKey('user.UserData', on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    class Meta:
        app_label = 'customer'
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

