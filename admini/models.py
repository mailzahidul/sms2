from django.db import models
from django.contrib.auth.models import User


class Emp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation_choice = (
        ('account', 'Account'),
    )
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    designation = models.CharField(choices=designation_choice, max_length=20)
