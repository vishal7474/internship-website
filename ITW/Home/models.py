from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50, null="true")
    intro=models.CharField(max_length=200, null="true")

    def __str__(self):
        return self.name


class Contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=400)
    date=models.DateField()

    def __str__(self):
        return self.name