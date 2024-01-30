from django import forms

class Alerta(forms.Form):
    mensaje = forms.CharField(widget=forms.Textarea)
      