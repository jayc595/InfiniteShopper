from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={}))

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'phone', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "The password does not match."
            )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
