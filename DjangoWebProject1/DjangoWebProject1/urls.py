from django.urls import include, re_path
import HelloDjangoApp.views 

from django.contrib import admin 
from django.urls import path 
from django.urls import path
from django.urls import path, include


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    re_path(r'^$', HelloDjangoApp.views.index, name='index'),
    re_path(r'^home$', HelloDjangoApp.views.index, name='home'),
    path('report/', HelloDjangoApp.views.report, name = 'report'),
]
