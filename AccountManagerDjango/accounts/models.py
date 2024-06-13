from django.core.validators import RegexValidator
from django.db import models

class User(models.Model):
    surname = models.CharField(max_length=100, blank=True, null=True, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')])
    name = models.CharField(max_length=100, blank=True, null=True, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')])
    patronymic = models.CharField(max_length=100, blank=True, null=True, validators=[RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')])
    birth_date = models.DateField(blank=True, null=True)
    passport_number = models.CharField(max_length=10, blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True, validators=[RegexValidator(r'^7\d{9}$', 'Phone number must be in the format 7XXXXXXXXX.')])
    email = models.EmailField(blank=True, null=True)
    registration_address = models.TextField(blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)