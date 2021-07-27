from django.conf.urls import url
from django.http import response
from django.conf.urls import url
from Student import views



urlpatterns=[
    url(r'^student$',views.studentapi),
    url(r'^student/([0-9]+)$',views.studentapi)
]