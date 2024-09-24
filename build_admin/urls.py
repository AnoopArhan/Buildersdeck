from django.urls import path
from . import views
urlpatterns =[
    path('bindex',views.index,name="bindex"),
    path('breg',views.build_adminregister,name="breg" ),
    path('blog',views.build_adminlogin,name="blog" ),
    path('booking',views.booking,name="booking" ),
    path('table',views.table,name="table" ),
    
    path('accept/<int:id>',views.accept,name="accept" ),
    path('reject/<int:id>',views.reject,name="reject" ),
    
    path('aquali/<int:id>',views.aqualification,name="aquali" ),
    path('cquali/<int:id>',views.cqualification,name="cquali" ),
    path('equali/<int:id>',views.equalification,name="equali" ),
    path('dquali/<int:id>',views.dqualification,name="dquali" ),
    path('squali/<int:id>',views.squalification,name="squali" ),
    
    path('uimg/<int:id>',views.uimage,name="uimg" ),

    
    
    
]