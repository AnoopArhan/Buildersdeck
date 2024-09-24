from django.db import models

# Create your models here.
class Shop_TB(models.Model):
    Email=models.EmailField(max_length=50,default='a@gmail.com')
    Category=models.CharField(max_length=50)
    Shop=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Licence=models.ImageField(max_length=50)
    Experience=models.IntegerField(default=2)
    shop_id=models.CharField(max_length=20,default=0)

    
    
    def __str__(self):
        return self.Shop
    
    
class Sproduct_TB(models.Model):
    Productimg=models.ImageField(upload_to="work")
    Pname=models.CharField(max_length=50,default="null")
    Price=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    # workid=models.ForeignKey(Contractor_TB,on_delete=models.CASCADE,default="1")
    workid=models.CharField(max_length=100,default='1')
    Workvid=models.FileField(upload_to="swork_vid",default='a.mp4')
    
    
            