from django import forms
from django.core.exceptions import ValidationError

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    fullname = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=13)
    message = forms.CharField(widget=forms.Textarea)
    subject = forms.CharField(max_length=200)

    def clean_fullname(self):
        data = self.cleaned_data['fullname']
        if "tulkin" not in data:
            raise ValidationError("Sani isming Tulkin emas!!")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

