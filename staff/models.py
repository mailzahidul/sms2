from django.db import models


class StaffRegistration(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    gender_choice = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=6, default='Male')
    dob = models.DateField()
    joining_date = models.DateField()
    address = models.TextField()
    photo = models.ImageField(upload_to='staff/')
    contact = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
