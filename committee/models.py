from django.db import models


class CommitteeInfo(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    photo = models.ImageField()
    address = models.TextField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name