from django import forms
from antispam.honeypot.forms import HoneypotField
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    nom = forms.CharField(max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    spam_honeypot_field = HoneypotField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)