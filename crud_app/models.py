from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(blank=True,null=True,unique=True)
    address=models.TextField()
    phone=models.IntegerField()

    def __str__(self) -> str:
        return self.name