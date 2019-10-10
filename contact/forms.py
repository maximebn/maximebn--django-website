from django import forms

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    nom = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)