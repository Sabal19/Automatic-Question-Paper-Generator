from django.contrib import admin
from django.urls import path
from . import views, ocrinsingleline
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve




admin.site.site_title = "Welcome to Admin Dashboard"
admin.site.site_header = "Login to Admin Panel"
admin.site.index_title = "Welcome to Admin Portal "

urlpatterns =[

    path('', views.home, name='home'),
    path('admin',views.admin, name='admin'),
    path('tologin',views.tologin, name = 'tologin'),
    path('login',views.login,name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout,name = 'logout'),
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('ocr_signal',ocrinsingleline.ocr_single,name='ocr_signal'),
    path('downloadfromhere',views.downloadfromhere, name = 'downloadfromhere'),
    path('getdata',views.getdata,name = 'getdata'),
    re_path('get_pdf',views.get_pdf,name='get_pdf')
    

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
