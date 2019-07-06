from django.db import models


class TecherInfo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender_choice = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6, default='Male')
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name
