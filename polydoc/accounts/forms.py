from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserloginForm(forms.Form):
    username = forms.CharField(label = "")
    password = forms.CharField(label = "", widget=forms.PasswordInput)






"""

class UserRegisterForm(forms.ModelForm):
    password = forms.CharFieldsWidget = forms.PasswordInput(attrs={"placeholder":"Enter password here"})
    confirm_password = forms.CharFieldsWidget = forms.PasswordInput(attrs={"placeholder":"Enter password here"})
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password Mismatch")
        return confirm_password
"""