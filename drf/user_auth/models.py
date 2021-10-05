from django.db import models

# Create your models here.

class registerUser(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    c_pass = models.CharField(max_length=8,default='')

    def __str__(self):
        return self.name

