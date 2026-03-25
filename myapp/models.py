from django.db import models


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"