# creating new file in rango app dir for
# remianing url string


from django.conf.urls import url
from rango import views
from django.conf.urls import url
from rango import views
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^about/', views.index, name='index'),
]


