from django.conf.urls import url, include
from . import views
from .models import Enquiry




urlpatterns = [
    url(r'^enquiry/', views.newEnquiry , name = 'New Enquiry'),
    url(r'^list/', views.index , name = 'list')
]