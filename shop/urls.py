from django.urls import path
from . import views
urlpatterns =[
    path('shome',views.sindex,name="shome"),
    path('shopregister',views.shopregister,name="shopregister" ),
    path('shoplogin',views.shoplogin,name="shoplogin" ),
    path('sproduct',views.sproduct,name="sproduct" ),
     path('sprofile',views.sprofile,name="sprofile"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('editproduct/<int:id>',views.editproduct,name="editproduct"),
    path('editprofile<str:id>',views.editprofile,name="editprofile"),
   
    path('S_chat/<int:uid>',views.S_chat,name="S_chat"),
    path('schat',views.chat,name="schat"),
    path('shopforpass',views.shopforpass,name="shopforpass" ),
    path('shopotp',views.shopotp,name="shopotp" ),
    path('shoprepass',views.shoprepass,name="shoprepass" ),
    
    
]