from django.conf.urls import url
from . import views


app_name='first_project'

urlpatterns=[
    url(r'^first_project/$',views.index.as_view(),name='index'),
    url(r'^first_project/(?P<pk>[0-9]+)/$',views.details.as_view(),name='details'),
    url(r'^first_project/form_data/$',views.formView,name='nameForm'),
    url(r'^first_project/create/$',views.create.as_view(),name='create'),
    url(r'^first_project/update/(?P<pk>[0-9]+)/$',views.update.as_view(),name='update'),
    url(r'^first_project/delete/(?P<pk>[0-9]+)/$', views.delete.as_view(), name='delete'),

]