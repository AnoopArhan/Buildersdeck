from django.db import models

# Create your models here.
class Astroleger_TB(models.Model):
    District=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,default='a@gmail.com')
    
    Place=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Qualification=models.ImageField(max_length=50)
    Experience=models.IntegerField(default=2)
    astro_id=models.CharField(max_length=20,default=0)
    
    
    
    def __str__(self):
        return self.Email
    
class ABook_TB(models.Model):
    
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,default='a@gmail.com')
    
    Number=models.CharField(max_length=50)
    # workid=models.ForeignKey(Contractor_TB,on_delete=models.CASCADE,default="1")
    astroid=models.CharField(max_length=100,default='1')
    userid=models.CharField(max_length=50)
    location=models.CharField(max_length=50,default=0)
    Pincode=models.CharField(max_length=50,default=0)
    Address=models.CharField(max_length=100,default=0)
    City=models.CharField(max_length=100,default=0)
    Landmark=models.CharField(max_length=100,default=0)
    time=models.CharField(max_length=20,default=0)
    date=models.CharField(max_length=20,default=0)
    
    accept=models.BooleanField(default="False")
    reject=models.BooleanField(default="False")
    fees=models.CharField(max_length=20,default="0")
        
    def __str__(self):
        return self.Name