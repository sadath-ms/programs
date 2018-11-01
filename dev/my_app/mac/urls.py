from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mac/$',views.index,name='index'),
]
