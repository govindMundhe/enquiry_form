from django.conf.urls import url, include
from . import views
from enquiry.views import indexView, enquiryCreate
from .models import Enquiry




urlpatterns = [
    # url(r'^enquiry/', views.newEnquiry , name = 'New Enquiry'),
    # url(r'^list/', views.index , name = 'list')
    url (r'^list/', indexView.as_view(), name = 'list'),
    url (r'^enquiry/',enquiryCreate.as_view(), name = 'New Enquiry' ),
]