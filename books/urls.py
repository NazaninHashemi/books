
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from Home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('contact', contactus),
    path('<str:idbook>/' , booktype),
    path('Story/<int:idinfo>/',infobook),
  path('History/<int:idinfo>/',infobook),
   path('user',userlogin),
  path('userpanel/',upanel),
   path('logout/',lout), 
    path('register',reg),
  
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
