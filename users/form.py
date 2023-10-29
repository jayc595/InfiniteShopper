from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={}))



    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
