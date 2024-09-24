from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
import os
from .models import *
from datetime import date,datetime
from buildproject.settings import EMAIL_HOST_USER
from user import forms
from django.core.mail import send_mail
import random
import string


# Create your views here.
def sindex(request):
    return render(request,'Shop/shome.html')
def shopregister(request):
    if request.method=="POST":
        name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Email=request.POST.get("Email")
        Gender=request.POST.get("Gender")
        Image=request.FILES.get('Image')
        Address=request.POST.get("Address")
        Category=request.POST.get("Category")
        Shop=request.POST.get("Shop")
        District=request.POST.get("District")
        Place=request.POST.get("Place")
        Pincode=request.POST.get("Pincode")
        Licence=request.FILES.get('Licence')
        Experience=request.POST.get("Experience")
        shop=request.POST.get("shop")
        
        p1=request.POST.get("Password")
        p2=request.POST.get("Cpass") 
        
        uname=shop + '_' + name
        if p1==p2:
            if Registration_TB.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exists')
            else:
                userdata=Registration_TB(Name=name,Mobile=Mobile,Email=Email,Gender=Gender,Image=Image,Address=Address,Password=p1,usertype=shop)
                userdata.save()
                sdata=Shop_TB(Email=Email,Shop=Shop,Category=Category,District=District,Place=Place,Pincode=Pincode,Licence=Licence,Experience=Experience)
                sdata.save()
                return redirect("shoplogin")
        else:
            messages.info(request,'password not match')
            error = "password not match !!"
    return render(request,'shop/shopreg.html')

def shoplogin(request): 
    error=None
    
    if request.method =="POST":
        messages.info(request,"post loop")
        try:
            messages.info(request,"try")
            
            Email=request.POST.get("Email")      
            password=request.POST.get("Password")
            shop=request.POST.get("shop")
            log=Registration_TB.objects.get(Email=Email,Password=password,usertype=shop)
            if log.accept:
            
                request.session['username']=log.Name
                request.session['id']=log.id
                Shop_TB.objects.filter(Email=Email).update( shop_id=log.id)
                return redirect('shome')
                
            else:
                messages.info(request,"Account Blocked")
                
        except Registration_TB.DoesNotExist as e :
            error = "Email or Password invalid !!"
            
    return render(request,'shop/shoplogin.html',{'error':error})

global bmi_value
bmi_value = 0

def  sproduct(request):
    if request.method=="POST":
        Productimg=request.FILES.get('Productimg')
        Pname=request.POST['Pname']
        Price=request.POST['Price']
        Description=request.POST['Description']
        pid=request.POST['pid']
        Workvid=request.FILES.get('Workvid')
        

        save_value=Sproduct_TB(Pname=Pname,Productimg=Productimg,Price=Price,Description=Description,workid=pid,Workvid=Workvid)
        save_value.save()
        return redirect('shome')

    return render(request,'Shop/product.html')


def sprofile(request):
    id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Sproduct_TB.objects.filter(workid=id)
    
    return render(request,'Shop/sprofile.html',{'pro':prof,'pros':pros})

def detail(request,id):
    
    pros=Sproduct_TB.objects.get(id=id)
    return render(request,'Shop/detail.html',{'pro':pros})

def editproduct(request,id):
    
    pros=Sproduct_TB.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            pros.Productimg=request.FILES.get('Productimg')
            pros.Workvid=request.FILES.get('Workvid')
            
        pros.Pname=request.POST['Pname']
        pros.Price=request.POST['Price']
        pros.Description=request.POST['Description']
        pros.save()
        return redirect("sprofile")
        
    return render(request,'Shop/editproduct.html',{'pro':pros})


def editprofile(request,id):
    
    reg=Registration_TB.objects.get(id=id)
    proccs= Shop_TB.objects.get(shop_id=id)
    
    if request.method=="POST":
        if len(request.FILES)!=0:
            
            reg.Image=request.FILES.get('Image')
        reg.Name=request.POST.get("Name")
        reg.Mobile=request.POST['Mobile']
        reg.Email=request.POST['Email']
        reg.Gender=request.POST['Gender']
        reg.Address=request.POST['Address']
        # proccs.Shop=request.POST['Shop']
        # proccs.Category=request.POST['Category']
        proccs.District=request.POST['District']
        proccs.Place=request.POST['Place']
        proccs.Pincode=request.POST['Pincode']
        proccs.Experience=request.POST['Experience']
        proccs.save()
        reg.save()
        return redirect("shome")
        
    return render(request,'Shop/editprofile.html',{'proccs':proccs,'proff':reg})

def S_chat(request,uid):
    
    aid=request.session['id']
    aname=request.session['username']
    udata=Registration_TB.objects.get(id=uid)
    rid=udata.id
    rname=udata.Name
    Mdata=Messages_Tb.objects.filter(Send_id=aid,Receiver_id=rid) | Messages_Tb.objects.filter(Send_id=rid,Receiver_id=aid) 
    
    cid=request.session['id']
    data=Messages_Tb.objects.filter(Receiver_id=cid)
    udata=[]
    Uid=[]
    for i in data:
        uid=i.Send_id
        Uid.append(i.Send_id)
    a=set(Uid)
    b=list(a)
    
    for i in b:
        uid=i
        udata.append(Registration_TB.objects.get(id=uid))
    
    if request.method == "POST":
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        message=request.POST.get("message")
        Rid=rid
        Sid=aid
        rname=rname
        sname=aname
        adata=Messages_Tb(Messages=message,Date=today,Time=current_time,Send_id=Sid,Receiver_id=Rid,Send_name=sname,Receiver_name=rname)
        adata.save()
        mdata=Messages_Tb.objects.filter(Send_id=Sid,Receiver_id=Rid) | Messages_Tb.objects.filter(Send_id=Rid,Receiver_id=Sid) 
       
        if Sid>8:
            Sid1=Sid-7    
        
        return render(request,'Shop/chating1.html',{'message':mdata,'Name':aname,'Rname':rname,'data':udata})
        
    if aid>8:
        aid1=aid-7
    else:
        aid1=aid

    return render(request,'Shop/chating1.html',{'message':Mdata,'Name':aname,'Rname':rname,'sid':aid1,'data':udata})

def chat(request):
    today = date.today()
    
    Aid=request.session['id']
    data=Messages_Tb.objects.filter(Receiver_id=Aid)
    udata=[]
    Uid=[]
    for i in data:
        uid=i.Send_id
        Uid.append(i.Send_id)
    a=set(Uid)
    b=list(a)
    for i in b:
        uid=i
        udata.append(Registration_TB.objects.get(id=uid))
        
        
    return render(request,'Shop/chating1.html',{'data':udata,'uid':Uid, 'b':b, 'date':today})
def shopforpass(request):
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


def shopotp(request):
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


def shoprepass(request):
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
