from django.urls import path
from . import views
urlpatterns =[
    path('ehome',views.eindex,name="ehome"),
    path('engineerregister',views.engineerregister,name="engineerregister" ),
    path('engineerlogin',views.engineerlogin,name="engineerlogin" ),
    path('ework',views.ework,name="ework"),
    path('eprofile',views.eprofile,name="eprofile"),
    path('e_detail/<int:id>',views.e_detail,name="e_detail"),
    path('e_editwork/<int:id>',views.e_editwork,name="e_editwork"),
    path('e_editprofile<str:id>',views.e_editprofile,name="e_editprofile"),

    path('E_chat/<int:uid>',views.E_chat,name="E_chat"),
    path('echat',views.chat,name="echat"),
    path('ebooking',views.viewbooking,name="ebooking" ),
    path('efees/<int:id>',views.fees,name="efees" ),
     path('engforpass',views.engforpass,name="engforpass" ),
    path('engotp',views.engotp,name="engotp" ),
    path('engrepass',views.engrepass,name="engrepass" ),
    
    
    
]