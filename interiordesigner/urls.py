from django.urls import path
from . import views
urlpatterns =[
    path('ihome',views.iindex,name="ihome"),
    path('designerregister',views.designerregister,name="designerregister" ),
    path('designerlogin',views.designerlogin,name="designerlogin" ),
    path('iwork',views.iwork,name="iwork"),
     path('iprofile',views.iprofile,name="iprofile"),
    path('i_detail/<int:id>',views.i_detail,name="i_detail"),
    path('i_editwork/<int:id>',views.i_editwork,name="i_editwork"),
    path('i_editprofile<str:id>',views.i_editprofile,name="i_editprofile"),
    
    path('D_chat/<int:uid>',views.D_chat,name="D_chat"),
    path('dchat',views.chat,name="dchat"),
    path('dbooking',views.viewbooking,name="dbooking" ),
    path('dfees/<int:id>',views.fees,name="dfees" ),
    path('dforpass',views.dforpass,name="dforpass" ),
    path('dotp',views.dotp,name="dotp" ),
    path('drepass',views.drepass,name="drepass" ),
    
    
    
]
