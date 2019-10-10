from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings

def contact(request):

    if request.method == 'POST' :
        form = ContactForm(request.POST)
        
        if form.is_valid(): 
            nom = form.cleaned_data['nom']
            sujet = form.cleaned_data['sujet']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['maximebn@posteo.ru']

            en_tete = 'Un nouveau message vient de vous être adressé par '+nom+' ('+email+') :\n'
            message = en_tete+'\n'+message

            send_mail(sujet, message, settings.EMAIL_HOST_USER, recipients)
            isMailSent = True
            return HttpResponseRedirect('/success') # Redirect after POST 

    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact/contact.html', locals())
