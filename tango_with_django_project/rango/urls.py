from django.conf.urls import url
from rango import views
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
     url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
]

