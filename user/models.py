from django.db import models

#Create your models here.
class Registration_TB(models.Model):
    Name=models.CharField(max_length=20,unique=True)
    Mobile=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Gender=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)
    Image=models.ImageField(upload_to="User")
    Password=models.CharField(max_length=15)
    usertype=models.CharField(max_length=50,default="user")
    accept=models.BooleanField(default="False")
    reject=models.BooleanField(default="False")
    
    
    
    
    def __str__(self):
        return self.Name
    
class Messages_Tb(models.Model):
    
    Messages=models.CharField(max_length=500)
    
    Date=models.DateField(max_length=10)
    Time=models.TimeField(max_length=50) 
    Send_id=models.CharField(max_length=50)
    Receiver_id=models.CharField(max_length=50)
    Send_name=models.CharField(max_length=50)
    Receiver_name=models.CharField(max_length=50)
    
    def __str__(self):

        return self.Send_name

    

