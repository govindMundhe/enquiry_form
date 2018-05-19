# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import EnquirySerializer
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from models import Enquiry
from django.urls import reverse_lazy

# def newEnquiry (request):
# 	if request.POST:
# 		form = EnquiryForm(request.POST)
# 		if form.is_valid():
# 			if form.save():
# 				return redirect('/list', messages.success(request, 'successfully created.', 'alert-success'))
# 			else:
# 				return redirect('/enquiry', messages.error(request, 'Data is not saved', 'alert-danger'))
# 		else:
# 			return redirect('/enquiry', messages.error(request, 'Form is not valid', 'alert-danger'))
# 	else:
# 		form = EnquiryForm()
# 	return render(request, 'enquiry.html', {'form':form})

# 	form = EnquiryForm()

class enquiryCreate (CreateView):
	model = Enquiry
	form_class = EnquiryForm
	template_name = 'enquiry.html'
	success_url = '/list'

# def index(request):
# 	hotels = Enquiry.objects.all()
# 	return render(request, 'list.html', {'hotels': hotels})

class indexView (ListView):
	model = Enquiry
	template_name = 'list.html'


class EnquiryViewSet(viewsets.ModelViewSet):
	queryset = Enquiry.objects.all()
	serializer_class = EnquirySerializer
 	"""
    API endpoint that allows users to be viewed or edited.
    """
    