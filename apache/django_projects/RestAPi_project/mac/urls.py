from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^mac/$',views.listGenericviews.as_view()),
    url(r'^mac/(?P<pk>[0-9]+)/$',views.detailsGenericviews.as_view()),
]