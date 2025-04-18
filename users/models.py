from django.db import models

class User(models.Model):
    id = models.CharField(max_length=9, primary_key=True)  # Israeli ID
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name