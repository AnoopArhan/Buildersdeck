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
def eindex(request):
    return render(request,'Engineer/ehome.html')
def engineerregister(request):
    # messages.info(request,'def loop')
    
    if request.method=="POST":
        # messages.info(request,'Post loop')
        
        name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Email=request.POST.get("Email")
        Gender=request.POST.get("Gender")
        Image=request.FILES.get('Image')
        Address=request.POST.get("Address")
        Company=request.POST.get("Company")
        District="Thrissur"
        Place=request.POST.get("Place")
        Pincode=request.POST.get("Pincode")
        Qualification=request.FILES.get('Qualification')
        Experience=request.POST.get("Experience")
        engineer=request.POST.get("engineer")
        
        p1=request.POST.get("Password")
        p2=request.POST.get("Cpass") 
        
        uname=engineer + '_' + name
        if p1==p2:
            
            
            if Registration_TB.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exists')
            else:
                
                
                userdata=Registration_TB(Name=name,Mobile=Mobile,Email=Email,Gender=Gender,Image=Image,Address=Address,Password=p1,usertype=engineer)
                userdata.save()
                edata=Engineer_TB(Email=Email,Company=Company,District=District,Place=Place,Pincode=Pincode,Qualification=Qualification,Experience=Experience)
                edata.save()
                return redirect("engineerlogin")
        else:
            messages.info(request,'password not match')
            error = "password not match !!"
        
    
    
    return render(request,'Engineer/engreg.html')
def engineerlogin(request):
    error=None
    
    if request.method =="POST":
    
        try: 
            
            
            Email=request.POST.get("Email")      
            password=request.POST.get("Password")
            engineer=request.POST.get("engineer")
            log=Registration_TB.objects.get(Email=Email,Password=password,usertype=engineer)
            if log.accept:
            
                request.session['username']=log.Name
                request.session['id']=log.id
                Engineer_TB.objects.filter(Email=Email).update(eng_id=log.id)
                return redirect('ehome')
            else:
                    messages.info(request," ")
        except Registration_TB.DoesNotExist as e :
            error = "Email or Password invalid !!"
    return render(request,'Engineer/englogin.html',{'error':error})
global bmi_value
bmi_value = 0


def  ework(request):
    if request.method=="POST":
        Workimg=request.FILES.get('Workimg')
        Workvid=request.FILES.get('Workvid')
        
        Feet=request.POST['Feet']
        Price=request.POST['Price']
        Description=request.POST['Description']
        eid=request.POST['eid']

        save_value=Ework_TB(Feet=Feet,workvid=Workvid,Workimg=Workimg,Price=Price,Description=Description,workid=eid,Workvid=Workvid)
        save_value.save()
        return redirect('ehome')

    return render(request,'Engineer/ework.html')
def eprofile(request):
    id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Ework_TB.objects.filter(workid=id)
    
    return render(request,'Engineer/eprofile.html',{'pro':prof,'pros':pros})

def e_detail(request,id):
    
    pros=Ework_TB.objects.get(id=id)
    return render(request,'Engineer/detail.html',{'pro':pros})

def e_editwork(request,id):
    
    pros=Ework_TB.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            pros.Workimg=request.FILES.get('Workimg')
            pros.workvid=request.FILES.get('Workvid')
            
        pros.Feet=request.POST['Feet']
        pros.Price=request.POST['Price']
        pros.Description=request.POST['Description']
        pros.save()
        return redirect("eprofile")
        
    return render(request,'Engineer/editwork.html',{'pro':pros})


def e_editprofile(request,id):
    
    reg=Registration_TB.objects.get(id=id)
    proccs= Engineer_TB.objects.get(eng_id=id)
    
    
    
    if request.method=="POST":
        if len(request.FILES)!=0:
          
            reg.Image=request.FILES.get('Image')
        reg.Name=request.POST.get("Name")
        reg.Mobile=request.POST['Mobile']
        reg.Email=request.POST['Email']
        reg.Gender=request.POST['Gender']
        reg.Address=request.POST['Address']
        proccs.Company=request.POST['Company']
        proccs.District=request.POST['District']
        proccs.Place=request.POST['Place']
        proccs.Pincode=request.POST['Pincode']
        proccs.Experience=request.POST['Experience']
        proccs.save()
        reg.save()
        return redirect("ehome")
        
    return render(request,'Engineer/editprofile.html',{'proccs':proccs,'proff':reg})

def E_chat(request,uid):
    
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
        
        return render(request,'Engineer/chating1.html',{'message':mdata,'Name':aname,'Rname':rname,'data':udata})
        
    if aid>8:
        aid1=aid-7
    else:
        aid1=aid
        
    return render(request,'Engineer/chating1.html',{'message':Mdata,'Name':aname,'Rname':rname,'sid':aid1,'data':udata})

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
        
        
    return render(request,'Engineer/chating1.html',{'data':udata,'uid':Uid, 'b':b, 'date':today})

def viewbooking(request):
    
    data=EBook_TB.objects.all()
    return render(request,'Engineer/booking.html',{'data':data})

def fees(request,id):
    if request.method=="POST":
        fees=request.POST.get("fees")
        EBook_TB.objects.filter(id=id).update(fees=fees)
        return redirect("ebooking")
    
    return render(request,'Engineer/fees.html')
def engforpass(request):
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


def engotp(request):
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


def engrepass(request):
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