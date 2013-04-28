from django import forms

class PunCreateForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
