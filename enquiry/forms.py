from django.forms import ModelForm
from django import forms
from .models import Enquiry

class DateInput(forms.DateInput):
	input_type = 'date'


class EnquiryForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'demo_date': DateInput(),
        }