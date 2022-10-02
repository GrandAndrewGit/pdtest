from django import forms
from .models import Profile
from django.forms import TextInput


class LoginForm(forms.Form):
    first_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'biography', 'contacts', 'date_of_birth']
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                }),
            'contacts': TextInput(attrs={
                'class': "form-control",
                }),
            'biography': TextInput(attrs={
                'class': "form-control",
                }),
            'date_of_birth': DateInput(),
        }



