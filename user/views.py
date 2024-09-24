from django.shortcuts import render,redirect
from . models import *
from contractor.models import *
from engineer.models import *
from interiordesigner.models import *
from astrologer.models import *
from shop.models import *
from django.db.models import F
from datetime import date,datetime
import os
from django.contrib import messages
from buildproject.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay 
from buildproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
import random
import string

# Create your views here.
def index(request):
    return render(request,'User/index.html')
def userregister(request):
    error=None
    if request.method=="POST":
        name=request.POST.get("Name")
        Mobile=request.POST.get("Mobile")
        Email=request.POST.get("Email")
        Gender=request.POST.get("Gender")
        Image=request.POST.get("img")
        Address=request.POST.get("Address")
        user=request.POST.get("user")
        
        p1=request.POST.get("password")
        p2=request.POST.get("cpassword") 
        
        if p1==p2:
            if Registration_TB.objects.filter(Email=Email).exists():
                messages.info(request,'Email Already Exists')
            else:
                userdata=Registration_TB(Name=name,Mobile=Mobile,Email=Email,Gender=Gender,Image=Image,Address=Address,Password=p1,usertype=user,accept="True")
                userdata.save()
                return redirect("userlogin")
        else:
            messages.info(request,'password not match')
            error = "password not match !!"
            return render(request,'user/userreg.html')
        
    return render(request,'user/userreg.html',{'error':error})
def userlogin(request):
    error=None
    if request.method =="POST":
        try:
            
            Email=request.POST.get("Email")      
            password=request.POST.get("password") 
            user=request.POST.get("user")
              
            log=Registration_TB.objects.get(Email=Email,Password=password,usertype=user)
            if log.accept:
                request.session['username']=log.Name
                request.session['id']=log.id
                return redirect('uindex')
            else:
                messages.info(request,"Account Blocked")
                
        except Registration_TB.DoesNotExist as e :
            error = "Email or Password invalid !!"
    return render(request,'User/userlogin.html',{'error':error})

global bmi_value
bmi_value = 0

def profile(request):
    hid=request.session['id']
    rdata=Registration_TB.objects.get(id=hid)
    return render(request,'User/profile.html', {'rdata':rdata})

def uprofile(request):
    cdata=Contractor_TB.objects.all()
    if request.method=="POST":
        disc=request.POST.get("search")
        cdata=Contractor_TB.objects.filter(District=disc)
    rdata=[]
    for data in cdata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/uprofile.html',{'rdata':rdata})

def ueprofile(request):
    edata=Engineer_TB.objects.all()
    if request.method=="POST":
        disc=request.POST.get("search")
        edata=Engineer_TB.objects.filter(District=disc)
    rdata=[]
    for data in edata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/eprofile.html',{'rdata':rdata})

def udprofile(request):
    ddata=Designer_TB.objects.all()
    if request.method=="POST":
        disc=request.POST.get("search")
        ddata=Designer_TB.objects.filter(District=disc)
    rdata=[]
    for data in ddata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/dprofile.html',{'rdata':rdata})

def uaprofile(request):
    ddata=Astroleger_TB.objects.all()
    if request.method=="POST":
        disc=request.POST.get("search")
        ddata=Astroleger_TB.objects.filter(District=disc)
    rdata=[]
    for data in ddata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/aprofile.html',{'rdata':rdata})

def tileprofile(request): 
    ddata=Shop_TB.objects.filter(Category="Tiles")
    if request.method=="POST":
        disc=request.POST.get("search")
        ddata=Shop_TB.objects.filter(District=disc)
    rdata=[]
    for data in ddata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/tileprofile.html',{'rdata':rdata})
 
def cementprofile(request):
    ddata=Shop_TB.objects.filter(Category="Cement")
    if request.method=="POST":
        disc=request.POST.get("search")
        ddata=Shop_TB.objects.filter(District=disc)
    rdata=[]
    for data in ddata:
        rdata.append(Registration_TB.objects.get(Email=data.Email))
    return render(request,'User/cementprofile.html',{'rdata':rdata})

def contractview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Cwork_TB.objects.filter(workid=id)
    
    return render(request,'User/contractview.html',{'pro':prof,'pros':pros})

def cworkview(request,id):
    
    pros=Cwork_TB.objects.get(id=id)
    return render(request,'User/cworkview.html',{'pro':pros})

def c_vid_play(request,id):
    
    pros=Cwork_TB.objects.get(id=id)
    return render(request,'User/c_vidplay.html',{'pro':pros})

def astroview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    # pros=Cwork_TB.objects.filter(workid=id)
    
    return render(request,'User/astroview.html',{'pro':prof})


def astrobook(request,id):
    from datetime import date
  
    # storing today's date in a variable
    today = date.today()
    import datetime
  
    today = datetime.datetime.now()
  
    # today=today.strftime('%d/%m/%Y')
    day=today.strftime('%d')
    mnth=today.strftime('%m')
    
    year=today.strftime('%Y')
    
    if request.method=="POST":
        Date=request.POST.get('date')
        Day=Date[0:2]

        Month=Date[3:5]

        YEAR=Date[6:10]

        if (Day < day) and (Month < mnth) and (YEAR < year):
            messages.info(request,'Select Valid date')
            Date=today
            
        
        else:
            Date=Date
            name=request.POST.get('Name')
            email=request.POST.get('Email')
            number=request.POST.get('Number')
            location=request.POST.get('location')
                    
            time=request.POST.get('time')
                    
                    
                
            uid=request.session['id']
            log=ABook_TB(Name=name,Email=email,Number=number,date=Date,location=location,time=time,astroid=id,userid=uid)
            log.save()
            return redirect('astroprof')
            
    return render(request,'User/astrobook.html')

def cbook(request,id):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        number=request.POST.get('Number')
        location=request.POST.get('location')
        
        time=request.POST.get('time')
        date=request.POST.get('date')
        
        uid=request.session['id']
        log=CBook_TB(Name=name,Email=email,Number=number,date=date,location=location,time=time,astroid=id,userid=uid)
        log.save()
        return redirect('uprof')
    
    return render(request,'User/cbook.html')

def ebook(request,id):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        number=request.POST.get('Number')
        location=request.POST.get('location')
        
        time=request.POST.get('time')
        date=request.POST.get('date')
        
        uid=request.session['id']
        log=EBook_TB(Name=name,Email=email,Number=number,date=date,location=location,time=time,astroid=id,userid=uid)
        log.save()
        return redirect('eprof')
    
    return render(request,'User/ebook.html')

def dbook(request,id):
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        number=request.POST.get('Number')
        location=request.POST.get('location')
        
        time=request.POST.get('time')
        date=request.POST.get('date')
        
        uid=request.session['id']
        log=DBook_TB(Name=name,Email=email,Number=number,date=date,location=location,time=time,astroid=id,userid=uid)
        log.save()
        return redirect('dprof')
    
    return render(request,'User/dbook.html')


def engineerview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Ework_TB.objects.filter(workid=id)
    
    return render(request,'User/engineerview.html',{'pro':prof,'pros':pros})

def eworkview(request,id):
    
    pros=Ework_TB.objects.get(id=id)
    return render(request,'User/eworkview.html',{'pro':pros})

def e_vid_play(request,id):
    
    pros=Ework_TB.objects.get(id=id)
    return render(request,'User/e_vidplay.html',{'pro':pros})

def designerview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Iwork_TB.objects.filter(workid=id)
    
    return render(request,'User/designerview.html',{'pro':prof,'pros':pros})

def dworkview(request,id):
    
    pros=Iwork_TB.objects.get(id=id)
    return render(request,'User/dwork.html',{'pro':pros})

def d_vid_play(request,id):
    
    pros=Cwork_TB.objects.get(id=id)
    return render(request,'User/d_vidplay.html',{'pro':pros})

def tilesview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Sproduct_TB.objects.filter(workid=id)
    
    return render(request,'User/tileview.html',{'pro':prof,'pros':pros})

def cementview(request,id):
    # id=request.session['id']
    prof=Registration_TB.objects.get(id=id)
    pros=Sproduct_TB.objects.filter(workid=id)
    
    return render(request,'User/cementview.html',{'pro':prof,'pros':pros})

def cementdetail(request,id):
    
    pros=Sproduct_TB.objects.get(id=id)
    return render(request,'User/cementdetail.html',{'pro':pros})

def tiledetail(request,id):
    
    pros=Sproduct_TB.objects.get(id=id)
    return render(request,'User/tiledetail.html',{'pro':pros})
def s_vid_play(request,id):
    
    pros=Sproduct_TB.objects.get(id=id)
    return render(request,'User/c_vidplay.html',{'pro':pros})

def clike(request,id):
    uid=request.session['id']
    
    data=Cwork_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    lflag=data.likeflag
    like=data.like
    dlike=data.dislike
    if like<2:
        if lflag:
            # Cwork_TB.objects.filter(id=id).update(like=F("like") + 1)
            Cwork_TB.objects.filter(id=id).update(likeflag=True)
        else:
            Cwork_TB.objects.filter(id=id).update(like=F("like") + 1)
            Cwork_TB.objects.filter(id=id).update(likeflag="True")
            if dlike>0:
                Cwork_TB.objects.filter(id=id).update(dislike=F("dislike") - 1)
                Cwork_TB.objects.filter(id=id).update(dislikeflag="False")
        
        
    
    # return redirect("uprof")
    return HttpResponseRedirect("contractview/%d"%wid)

def cdislike(request,id):
    uid=request.session['id']
    
    data=Cwork_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    dslike=data.dislikeflag
    like=data.like
    dlike=data.dislike
    if dlike<2:
        if dslike:
            # Cwork_TB.objects.filter(id=id).update(dislike=F("dislike") + 1)
            Cwork_TB.objects.filter(id=id).update(userid=uid)
        else:
            Cwork_TB.objects.filter(id=id).update(dislike=F("dislike") + 1)
            Cwork_TB.objects.filter(id=id).update(dislikeflag="True")
            if like<2:
                Cwork_TB.objects.filter(id=id).update(likeflag="False")
                
                Cwork_TB.objects.filter(id=id).update(like=F("like") - 1)

    
    
    
    return HttpResponseRedirect("contractview/%d"%wid)


   
# def cdislike(request,id):
    
#     data=Cwork_TB.objects.get(id=id)
#     dislike=data.dislike
#     dislike=dislike+1
#     Cwork_TB.objects.filter(id=id).update(dislike=models.F('dislike')+1)
        
#     return render(request,'User/contractview.html')
from django.http import HttpResponseRedirect
def dlike(request,id):
    uid=request.session['id']
    
    data=Iwork_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    
    if userid=="0":
        Iwork_TB.objects.filter(id=id).update(like=F("like") + 1)
        Iwork_TB.objects.filter(id=id).update(userid=uid)

    return HttpResponseRedirect("designerview/%d"%wid)
   
def ddislike(request,id):
    uid=request.session['id']
    
    data=Iwork_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    
    if userid=="0":
        Iwork_TB.objects.filter(id=id).update(dislike=F("dislike") + 1)
        Iwork_TB.objects.filter(id=id).update(userid=uid)
        
    return HttpResponseRedirect("designerview/%d"%wid)

def elike(request,id):
    uid=request.session['id']
    
    data=Ework_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    
    if userid=="0":
        Ework_TB.objects.filter(id=id).update(like=F("like") + 1)
        Ework_TB.objects.filter(id=id).update(userid=uid)
        
    return HttpResponseRedirect("engineerview/%d"%wid)
   
def edislike(request,id):
    
    uid=request.session['id']
    
    data=Ework_TB.objects.get(id=id)
    userid=data.userid
    wid=int(data.workid)
    
    if userid=="0":
        Ework_TB.objects.filter(id=id).update(dislike=F("dislike") + 1)
        Ework_TB.objects.filter(id=id).update(userid=uid)
    
        
    return HttpResponseRedirect("engineerview/%d"%wid)

    
def User_chat(request,aid):
    uid=request.session['id']
    uname=request.session['username']
    adata=Registration_TB.objects.get(id=aid)
    rid=adata.id
    Mdata=Messages_Tb.objects.filter(Send_id=uid,Receiver_id=rid) | Messages_Tb.objects.filter(Send_id=rid,Receiver_id=uid) 
    rname=adata.Name
    if request.method == "POST":
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        message=request.POST.get("message")
        Rid=rid
        Sid=uid
        rname=rname
        sname=uname
        adata=Messages_Tb(Messages=message,Date=today,Time=current_time,Send_id=Sid,Receiver_id=Rid,Send_name=sname,Receiver_name=rname)
        adata.save()
        mdata=Messages_Tb.objects.filter(Send_id=Sid,Receiver_id=Rid) | Messages_Tb.objects.filter(Send_id=Rid,Receiver_id=Sid) 
        return render(request,'User/chat1.html',{'message':mdata,'Name':uname,'Rname':rname,'sid':Sid})
        
        
        # return redirect('chat')
    return render(request,'User/chat1.html',{'message':Mdata,'Name':uname,'Rname':rname,'sid':uid})


def ccomment(request,id):
    uid=request.session['id']
    name=request.session['username']
    a=Ccomment.objects.filter(to_id=id)
    if request.method=="POST":
        time=datetime.now()
        # _date(datetime.now(), "d b, D")
        # t=time.strftime("%Y/%m/%d, %H:%M:%S")
        comment=request.POST['comment']
        fid=uid
        tid=id
        pros=Ccomment(comment=comment,from_id=fid,to_id=tid,time=time,name=name)
        pros.save()
        a=Ccomment.objects.filter(to_id=id)
        return render(request,'User/comment.html',{'pro':a,'name':name})
    
    return render(request,'User/comment.html',{'pro':a})

def dcomment(request,id):
    uid=request.session['id']
    name=request.session['username']
    a=Dcomment.objects.filter(to_id=id)
    if request.method=="POST":
        time=datetime.now()
        # _date(datetime.now(), "d b, D")
        # t=time.strftime("%Y/%m/%d, %H:%M:%S")
        comment=request.POST['comment']
        fid=uid
        tid=id
        pros=Dcomment(comment=comment,from_id=fid,to_id=tid,time=time,name=name)
        pros.save()
        a=Dcomment.objects.filter(to_id=id)
        return render(request,'User/comment.html',{'pro':a,'name':name})
    
    return render(request,'User/comment.html',{'pro':a})

def ecomment(request,id):
    uid=request.session['id']
    name=request.session['username']
    a=Ecomment.objects.filter(to_id=id)
    if request.method=="POST":
        time=datetime.now()
        # _date(datetime.now(), "d b, D")
        # t=time.strftime("%Y/%m/%d, %H:%M:%S")
        comment=request.POST['comment']
        fid=uid
        tid=id
        pros=Ecomment(comment=comment,from_id=fid,to_id=tid,time=time,name=name)
        pros.save()
        a=Ecomment.objects.filter(to_id=id)
        return render(request,'User/comment.html',{'pro':a,'name':name})
    
    return render(request,'User/comment.html',{'pro':a})

def edit(request,id):
    
    reg=Registration_TB.objects.get(id=id)
    
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(reg.Image)>0:
                os.remove(reg.Image.path)
            reg.Image=request.FILES.get('Image')
        reg.Name=request.POST.get("Name")
        reg.Mobile=request.POST['Mobile']
        reg.Email=request.POST['Email']
        reg.Gender=request.POST['Gender']
        reg.Address=request.POST['Address']
        reg.Password=request.POST['Password']
        
        # proccs.Company=request.POST['Company']
        # proccs.District=request.POST['District']
        # proccs.Place=request.POST['Place']
        # proccs.Pincode=request.POST['Pincode']
        # proccs.Experience=request.POST['Experience']
        # proccs.save()
        reg.save()
        return redirect("uindex")
        
    return render(request,'User/edit.html',{'proff':reg})


def ubooking(request):
    id=request.session['id']
    data=ABook_TB.objects.filter(userid=id)
    return render(request,'User/ubooking.html',{'data':data})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def apay(request,id):
    uid=request.session['id']
    global amount
    data=ABook_TB.objects.get(id=id)
    amount=data.fees
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/checkout.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def cpay(request,id):
    uid=request.session['id']
    global amount
    data=CBook_TB.objects.get(id=id)
    amount=data.fees
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/checkout.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def epay(request,id):
    uid=request.session['id']
    global amount
    data=EBook_TB.objects.get(id=id)
    amount=data.fees
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/checkout.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def dpay(request,id):
    uid=request.session['id']
    global amount
    data=DBook_TB.objects.get(id=id)
    amount=data.fees
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'User/checkout.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def ddbook(request):
    id=request.session['id']
    
    data=DBook_TB.objects.filter(userid=id)
    return render(request,'User/dbooking.html',{'data':data})

def ccbook(request):
    id=request.session['id']
    
    data=CBook_TB.objects.filter(userid=id)
    return render(request,'User/cbooking.html',{'data':data})

def eebook(request):
    id=request.session['id']
    
    data=EBook_TB.objects.filter(userid=id)
    return render(request,'User/ebooking.html',{'data':data})

def aabook(request):
    id=request.session['id']
    
    data=ABook_TB.objects.filter(userid=id)
    return render(request,'User/abooking.html',{'data':data})


def userforpass(request):
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


def userotp(request):
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


def userrepass(request):
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
