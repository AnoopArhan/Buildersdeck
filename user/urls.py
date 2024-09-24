from django.urls import path
from . import views
urlpatterns = [
    path('uindex',views.index,name="uindex"),
    path('userregister',views.userregister,name="userregister" ),
    path('userlogin',views.userlogin,name="userlogin" ),
    path('prof',views.profile,name="prof" ),
    
    path('uprof',views.uprofile,name="uprof" ),
    path('dprof',views.udprofile,name="dprof" ),
    path('astroprof',views.uaprofile,name="astroprof"),
    path('tileprof',views.tileprofile,name="tileprof"),
    path('cementprof',views.cementprofile,name="cementprof"),
    
    path('eprof',views.ueprofile,name="eprof" ),
    path('contractview/<int:id>',views.contractview,name="contractview"),
    path('cworkview/<int:id>',views.cworkview,name="cworkview"),
    path('clike/contractview/<int:id>',views.contractview,name="clike/contractview"),
    path('cdislike/contractview/<int:id>',views.contractview,name="cdislike/contractview"),
    
    path('astroview/<int:id>',views.astroview,name="astroview"), 
    # path('aworkview/<int:id>',views.aworkview,name="aworkview"),
    path('astrobook/<int:id>',views.astrobook,name="astrobook"),
    path('cbook/<int:id>',views.cbook,name="cbook"),
    path('ebook/<int:id>',views.ebook,name="ebook"),
    path('dbook/<int:id>',views.dbook,name="dbook"),
    
    
    
    path('engineerview/<int:id>',views.engineerview,name="engineerview"),
    path('eworkview/<int:id>',views.eworkview,name="eworkview"),
    path('elike/engineerview/<int:id>',views.engineerview,name="elike/engineerview"),
    path('edislike/engineerview/<int:id>',views.engineerview,name="edislike/engineerview"),
    
    path('designerview/<int:id>',views.designerview,name="designerview"),
    path('dworkview/<int:id>',views.dworkview,name="dworkview"),
    
    path('tilesview/<int:id>',views.tilesview,name="tilesview"),
    path('cementview/<int:id>',views.cementview,name="cementview"),
    
    path('cementdet/<int:id>',views.cementdetail,name="cementdet"),
    path('tiletdet/<int:id>',views.tiledetail,name="tiledet"),
    
    path('c_vid_play/<int:id>',views.c_vid_play,name="c_vid_play"),
    path('d_vid_play/<int:id>',views.d_vid_play,name="d_vid_play"),
    path('e_vid_play/<int:id>',views.e_vid_play,name="e_vid_play"),
    path('s_vid_play/<int:id>',views.s_vid_play,name="s_vid_play"),
    
    path('clike/<int:id>',views.clike,name='clike'),
    path('dlike/designerview/<int:id>',views.designerview,name="dlike/designerview"),
    path('ddislike/designerview/<int:id>',views.designerview,name="ddislike/designerview"),
    
    path('dlike/<int:id>',views.dlike,name='dlike'),
    path('elike/<int:id>',views.elike,name='elike'),
    
    path('cdislike/<int:id>',views.cdislike,name='cdislike'),
    path('ddislike/<int:id>',views.ddislike,name='ddislike'),
    path('edislike/<int:id>',views.edislike,name='edislike'),
    
    path('User_chat/<int:aid>',views.User_chat,name='User_chat'),
    path('ccomment/<int:id>',views.ccomment,name='ccomment'),
    path('dcomment/<int:id>',views.dcomment,name='dcomment'),
    path('ecomment/<int:id>',views.ecomment,name='ecomment'),
    
    path('edit<str:id>',views.edit,name="edit"),
    path('ubooking',views.ubooking,name="ubooking"),
    path('apay/<int:id>',views.apay,name="apay"),
    path('cpay/<int:id>',views.cpay,name="cpay"),
    path('epay/<int:id>',views.epay,name="epay"),
    path('dpay/<int:id>',views.dpay,name="dpay"),
    
    
    path('ccbook',views.ccbook,name="ccbook" ),
    path('ddbook',views.ddbook,name="ddbook" ),
    path('eebook',views.eebook,name="eebook" ),
    path('aabook',views.aabook,name="aabook" ),
    path('userforpass',views.userforpass,name="userforpass" ),
    path('userotp',views.userotp,name="userotp" ),
    path('userrepass',views.userrepass,name="userrepass" ),
    
    
    
]