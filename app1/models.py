from django.db import models


class customerInquiry(models.Model):
    accountName = models.TextField(max_length=32)
    email = models.EmailField()
    birthDate = models.DateField()
    message = models.TextField()

class registerModel(models.Model):
    accountName = models.TextField(max_length=64)
    password = models.TextField(max_length=64)
    email = models.EmailField(max_length=32)
    birthDate = models.DateField(max_length=32)
    localArea = models.TextField(max_length=32)