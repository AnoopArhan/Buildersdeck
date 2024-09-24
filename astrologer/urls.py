from django.urls import path
from . import views
urlpatterns =[
    path('ahome',views.aindex,name="ahome"),
    path('astrologerregister',views.astrologerregister,name="astrologeregister" ),
    path('astrologerlogin',views.astrologerlogin,name="astrologerlogin" ),
    path('vbooking',views.viewbooking,name="vbooking" ),
    path('saccept/<int:id>',views.saccept,name="saccept" ),
    path('aprofile',views.aprofile,name="aprofile"),
    path('a_editprofile<str:id>',views.a_editprofile,name="a_editprofile"),
    path('sreject/<int:id>',views.sreject,name="sreject" ),
    path('fees/<int:id>',views.fees,name="fees" ),
    
 path('astroforpass',views.astroforpass,name="astroforpass" ),
    path('astrootp',views.astrootp,name="astrootp" ),
    path('astrorepass',views.astrorepass,name="astrorepass" ),
    
]