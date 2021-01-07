from django import forms
from django.core.exceptions import ValidationError
from .models import Feedback

class ProductForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'fullname',
            'email',
            'phone_number',
            'message'
        ]
