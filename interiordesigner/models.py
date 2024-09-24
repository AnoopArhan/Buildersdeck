from django.db import models

# Create your models here.
class Designer_TB(models.Model):
    Email=models.EmailField(max_length=50,default='a@gmail.com')
    Company=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Licence=models.ImageField(max_length=50)
    Experience=models.IntegerField(default=2)
    design_id=models.CharField(max_length=20,default=0)

    
    
    def __str__(self):
        return self.Company




class Iwork_TB(models.Model):
    Workimg=models.ImageField(upload_to="work")
    Feet=models.CharField(max_length=50,default="null")
    Price=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    # workid=models.ForeignKey(Contractor_TB,on_delete=models.CASCADE,default="1")
    workid=models.CharField(max_length=100,default='1')
    workvid=models.FileField(upload_to="cwork_vid",default='a.mp4')
    userid=models.CharField(max_length=100,default=0)
    
    like=models.IntegerField(default="0")
    dislike=models.IntegerField(default="0")
    
        
        
    def __str__(self):
        return self.Feet
    
class Dcomment(models.Model):
    
    name=models.CharField(max_length=50,default="user")
    from_id=models.CharField(max_length=50)
    to_id=models.CharField(max_length=50)
    comment=models.CharField(max_length=50)
    time=models.DateTimeField(null="True")
    
    def __str__(self):
        return self.from_id
    
class DBook_TB(models.Model):
    
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,default='a@gmail.com')
    
    Number=models.CharField(max_length=50)
    # workid=models.ForeignKey(Contractor_TB,on_delete=models.CASCADE,default="1")
    astroid=models.CharField(max_length=100,default='1')
    userid=models.CharField(max_length=50)
    location=models.CharField(max_length=50,default=0)
    
    time=models.CharField(max_length=20,default=0)
    date=models.CharField(max_length=20,default=0)
    
    accept=models.BooleanField(default="False")
    reject=models.BooleanField(default="False")
    fees=models.CharField(max_length=20,default="0")
        
    def __str__(self):
        return self.Name
