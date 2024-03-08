from django.db import models

# Create your models here.
class student(models.Model):
    NAME=models.CharField(max_length=15)
    ENROLLMENTNUMBER=models.IntegerField()
    COURSE=models.CharField(max_length=20)
    MOBILE=models.CharField(max_length=10)
    EMAIL=models.EmailField()

    def __str__(self):
        return self.NAME
    
class employee(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    salary=models.CharField(max_length=7)

    def __str__(self):
        return self.firstname