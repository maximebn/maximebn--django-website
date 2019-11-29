from django.test import TestCase
from contact.forms import ContactForm
from django.urls import reverse

class ContactTests(TestCase):

    def test_valid_form(self):
        form_data = {'sujet': 'Test subject', 'nom':'MyName', 'email':'myname@mail.com', 'message':'Here is a sample message'}
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_blank_data(self):
        form = ContactForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
        'sujet': ['Ce champ est obligatoire.'],
        'nom': ['Ce champ est obligatoire.'],
        'email': ['Ce champ est obligatoire.'],
        'message': ['Ce champ est obligatoire.']
    })

    def test_unvalid_mail(self):
        form = ContactForm({'sujet': 'Test subject', 'nom':'MyName', 'email':'mynamemail.com', 'message':'Here is a sample message'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
        'email': ['Saisissez une adresse de courriel valide.'],
    })

class ContactViewTests(TestCase):
    
    def test_normal_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_view_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')