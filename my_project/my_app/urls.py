from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf.urls import url

#TEMPLATE TAGGING
app_name='my_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
