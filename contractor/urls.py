from django.urls import path
from . import views
urlpatterns =[
    path('chome',views.cindex,name="chome"),
    path('contractregister',views.contractregister,name="contractregister" ),
    path('contractlogin',views.contractlogin,name="contractlogin" ),
    path('cwork',views.cwork,name="cwork"),
    path('cprofile',views.cprofile,name="cprofile"),
    path('C_detail/<int:id>',views.C_detail,name="C_detail"),
    path('C_editwork/<int:id>',views.C_editwork,name="C_editwork"),
    path('C_editprofile<str:id>',views.C_editprofile,name="C_editprofile"),
    
    path('C_chat/<int:uid>',views.C_chat,name="C_chat"),
    path('cchat',views.chat,name="cchat"),
    path('cbooking',views.viewbooking,name="cbooking" ),
    path('cfees/<int:id>',views.fees,name="cfees" ),
    path('contraforpass',views.contraforpass,name="contraforpass" ),
    path('contraotp',views.contraotp,name="contraotp" ),
    path('contrarepass',views.contrarepass,name="contrarepass" ),
    
    
    
    
    path('uscomment/<int:id>',views.usercomment,name='uscomment'),
    
    
    
    
    
    
    # path('cimg',views.cimg,name="cimg"),
    
    
]