from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
import os
from .models import *
from buildproject.settings import EMAIL_HOST_USER
from user import forms
from django.core.mail import send_mail
import random
import string
# Create your views here.
def aindex(request):
    return render(request,'Astrologer/ahome.html')
def astrologerregister(request):
    
    if request.method=="POST":
        name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Email=request.POST.get("Email")
        Gender=request.POST.get("Gender")
        Image=request.FILES.get('Image')
        Address=request.POST.get("address")
        District=request.POST.get("District")
        Place=request.POST.get("Place")
        Pincode=request.POST.get("Pincode")
        Qualification=request.FILES.get('Qualification')
        Experience=request.POST.get("Experience")
        astrologer=request.POST.get("astrologer")
        
        p1=request.POST.get("Password")
        p2=request.POST.get("Cpass") 
        
        uname=astrologer + '_' + name
        if p1==p2:
            if Registration_TB.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exists')
            else:
                userdata=Registration_TB(Name=uname,Mobile=Mobile,Email=Email,Gender=Gender,Image=Image,Address=Address,Password=p1,usertype=astrologer)
                userdata.save()
                adata=Astroleger_TB(Email=Email,District=District,Place=Place,Pincode=Pincode,Qualification=Qualification,Experience=Experience,Price=Price,Travelling=Travelling)
                adata.save()
                return redirect("astrologerlogin")
        else:
            messages.info(request,'password not match')
            error = "password not match !!"
    return render(request,'Astrologer/astroreg.html')

def astrologerlogin(request):
    error=None
    
    if request.method =="POST":
        messages.info(request,"post loop")
        try:
            messages.info(request,"try")
            Email=request.POST.get("Email")      
            password=request.POST.get("Password")
            astrologer=request.POST.get("astrologer")
            
            log=Registration_TB.objects.get(Email=Email,Password=password,usertype=astrologer)
            if log.accept:
                
                request.session['username']=log.Name
                request.session['id']=log.id
                Astroleger_TB.objects.filter(Email=Email).update(astro_id=log.id)
                return redirect('ahome')
                
            else:
                messages.info(request,"Account Blocked")
        except Registration_TB.DoesNotExist as e :
            error = "Email or Password invalid !!"
    return render(request,'Astrologer/astrologin.html',{'error':error})
global bmi_value
bmi_value = 0

def viewbooking(request):
    
    data=ABook_TB.objects.all()
    return render(request,'Astrologer/booking.html',{'data':data})
    
def saccept(request,id):
    
    ABook_TB.objects.filter(id=id).update(accept=True)
    ABook_TB.objects.filter(id=id).update(reject=False)
    
    return redirect("vbooking")

def sreject(request,id):
    
    ABook_TB.objects.filter(id=id).update(reject=True)
    ABook_TB.objects.filter(id=id).update(accept=False)
    
    return redirect("vbooking")

def fees(request,id):
    if request.method=="POST":
        fees=request.POST.get("fees")
        ABook_TB.objects.filter(id=id).update(fees=fees)
        return redirect("vbooking")
    
    return render(request,'Astrologer/fees.html')
    
def aprofile(request):
    id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
   
    return render(request,'Astrologer/aprofile.html',{'pro':prof})
    
  
def a_editprofile(request,id):
    
    reg=Registration_TB.objects.get(id=id)
    proccs=Astroleger_TB.objects.get(astro_id=id)  
    if request.method=="POST":
        if len(request.FILES)!=0:
            
            reg.Image=request.FILES.get('Image')
        reg.Name=request.POST.get("Name")
        reg.Mobile=request.POST['Mobile']
        reg.Email=request.POST['Email']
        reg.Gender=request.POST['Gender']
        reg.Address=request.POST['Address']
        proccs.District=request.POST['District']
        proccs.Place=request.POST['Place']
        proccs.Pincode=request.POST['Pincode']
        proccs.Experience=request.POST['Experience']
        proccs.Price=request.POST['Price']
        proccs.Travelling=request.POST['Travelling']
        proccs.save()
        reg.save()
        return redirect("ahome")
        
    return render(request,'Astrologer/editprofile.html',{'proccs':proccs,'proff':reg})
def astroforpass(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = request.POST['email']
        name= request.POST['name']
        subject = 'Hi, '+format(name) 
        recepient = str(sub)
      
        # get random password pf length 8 with letters, digits, and symbols
        characters =  string.digits 
        password = ''.join(random.choice(characters) for i in range(6))
        Registration_TB.objects.filter(Email=sub).update(Password=password)
        
        message = '''Welcome to BUILDERSDECK site.
        The OTP is : ''' +format(password)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return redirect('userotp')
    return render(request,'User/userforpass.html')


def astrootp(request):
    error_message=None 
    if request.method == 'POST':
        try:
            otp = request.POST['otp']
            log=Registration_TB.objects.get(Password=otp)
            

            request.session['username']=log.Name
            request.session['id']=log.id

            return redirect('userrepass')
        except Registration_TB.DoesNotExist as e :
            error_message='name or password invalid'
    return render(request,'User/userotp.html')                                                                               


def astrorepass(request):
    id=request.session['id']
    if request.method == 'POST':
        password = request.POST['password']
        cpassword= request.POST['cpassword']
        if password==cpassword:
            Registration_TB.objects.filter(id=id).update(Password=password)
            return redirect('userlogin')
        else:
            messages.info(request,'Password not match')
    return render(request,'User/userrepass.html') 