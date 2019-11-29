from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import BadHeaderError, send_mail, mail_admins
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from maximebn import staticAttributes
from datetime import datetime

def contact(request):

    if request.method == 'POST' :
        form = ContactForm(request.POST)
        
        if form.is_valid(): 
            nom = form.cleaned_data['nom']
            sujet = form.cleaned_data['sujet']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = [email]

            en_tete = staticAttributes.EMAIL_HEADER + nom + ' ('+email+') :\n'
            message_to_send = en_tete+'\n'+message

            #Mail confirmation parameters

            sujet_confirmation = staticAttributes.EMAIL_CONFIMATION_SUBJECT
            message_confirmation = staticAttributes.EMAIL_CONFIRMATION_MESSAGE
            message_confirmation += '\n\n' + staticAttributes.EMAIL_SEPARATOR + '\n\nMessage received: ' + datetime.now().isoformat() + '\n\n' + message

            try:
                mail_admins(sujet, message_to_send, fail_silently=True)
                send_mail(sujet_confirmation, message_confirmation, settings.EMAIL_HOST_USER, recipients)
                isMailSent = True
            except BadHeaderError:
                return HttpResponse('Bad header found...')
            return HttpResponseRedirect('/success') # Redirect after POST 

    else:
        form = ContactForm() # An unbound form

    return render(request, 'contact/contact.html', locals())
