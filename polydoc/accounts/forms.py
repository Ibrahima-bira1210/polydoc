from django import forms

from .models import *


class UserloginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class mat_ens(forms.ModelForm):
    mat_ens = forms.ModelMultipleChoiceField(
        queryset=Matiere.objects.all()
    )


class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('matiere_doc', 'type_doc', 'title', 'extension_doc', 'author', 'pdf')
