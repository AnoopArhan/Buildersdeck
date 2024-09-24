from django.shortcuts import render,redirect
from . models import *
from contractor.models import *
from user.models import *
from engineer.models import *
from interiordesigner.models import *
from astrologer.models import *
from shop.models import *
from django.db.models import F
from datetime import date,datetime
import os
from django.contrib import messages

# Create your views here.
def index(request):
    
    data=Registration_TB.objects.all()
    ucount=Registration_TB.objects.filter(usertype="user")
    
    ccount=Contractor_TB.objects.all()
    dcount=Designer_TB.objects.all()
    acount=Astroleger_TB.objects.all()
    scount=Shop_TB.objects.all()
    ecount=Engineer_TB.objects.all()
    return render(request,'Admin/index.html',{'data':data,'acount':acount,'ccount':ccount,'dcount':dcount,'scount':scount,'ecount':ecount,'ucount':ucount})

def build_adminregister(request):
    if request.method=="POST":
        name=request.POST.get("Name")
        Email=request.POST.get("Email")
        
        p1=request.POST.get("Password")
        p2=request.POST.get("cpassword") 
        
        if p1==p2:
            if Admin_db.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exists')
            else:
                data=Admin_db(Name=name,Email=Email,Password=p1)
                data.save()
                return redirect("blog")
        else:
            messages.info(request,'password not match')
            return render(request,'Admin/adminreg.html')
        
    return render(request,'Admin/adminreg.html')

def build_adminlogin(request):
    if request.method =="POST":
        try:
            
            Email=request.POST.get("Email")      
            password=request.POST.get("Password") 
              
            log=Admin_db.objects.get(Email=Email,Password=password)
            request.session['username']=log.Name
            request.session['id']=log.id
            return redirect('bindex')
        except Admin_db.DoesNotExist as e :
            messages.info(request,"Invalid User")
            
    return render(request,'Admin/adminlogin.html')


# def table(request):
#     uid=request.session['id']
#     udata=Registration_TB.objects.all()
#     return render(request,'Admin/adminlogin.html',{'udata':udata})
    
def booking(request):
    
    data=Registration_TB.objects.all()
    return render(request,'Admin/index.html',{'data':data})

def table(request):
    udata=Registration_TB.objects.filter(usertype="user")
    cdata=Registration_TB.objects.filter(usertype="contractor")
    adata=Registration_TB.objects.filter(usertype="astrologer")
    ddata=Registration_TB.objects.filter(usertype="designer")
    sdata=Registration_TB.objects.filter(usertype="shop")
    edata=Registration_TB.objects.filter(usertype="engineer")
    contractor=Contractor_TB.objects.all()
    Interior=Designer_TB.objects.all()
    Astrologer=Astroleger_TB.objects.all()
    Shop=Shop_TB.objects.all()
    engineer=Engineer_TB.objects.all()
    
    
    return render(request,'Admin/table.html',{'udata':udata,'cdata':cdata,'adata':adata,'ddata':ddata,'sdata':sdata,'edata':edata,'contractor':contractor,'Interior':Interior,'Astrologer':Astrologer,'shop':Shop,'engineer':engineer})

def accept(request,id):
    
    Registration_TB.objects.filter(id=id).update(accept=True)
    Registration_TB.objects.filter(id=id).update(reject=False)
    
    return redirect("bindex")

def reject(request,id):
    
    Registration_TB.objects.filter(id=id).update(reject=True)
    Registration_TB.objects.filter(id=id).update(accept=False)
    
    return redirect("bindex")

def aqualification(request,id):
    data=Astroleger_TB.objects.get(id=id)
    image=data.Qualification
    return render(request,"Admin/image.html",{'img':image})
def cqualification(request,id):
    data=Contractor_TB.objects.get(id=id)
    image=data.Licence
    return render(request,"Admin/image.html",{'img':image})
def equalification(request,id):
    data=Engineer_TB.objects.get(id=id)
    image=data.Qualification
    return render(request,"Admin/image.html",{'img':image})
def dqualification(request,id):
    data=Designer_TB.objects.get(id=id)
    image=data.Licence
    return render(request,"Admin/image.html",{'img':image})
def squalification(request,id):
    data=Shop_TB.objects.get(id=id)
    image=data.Licence
    return render(request,"Admin/image.html",{'img':image})
def uimage(request,id):
    data=Registration_TB.objects.get(id=id)
    image=data.Image
    return render(request,"Admin/image.html",{'img':image})
    