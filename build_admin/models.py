from django.db import models

# Create your models here.
class Admin_db(models.Model):
    Name=models.CharField(max_length=20,unique=True)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=15)
    
    def __str__(self):
        return self.Name