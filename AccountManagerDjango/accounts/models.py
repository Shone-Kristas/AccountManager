from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    birth_date = models.DateField()
    passport_number = models.CharField(max_length=10)
    birth_place = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    registration_address = models.TextField()
    residential_address = models.TextField()