from django.test import TestCase
from contact.forms import ContactForm

class ContactTests(TestCase):

    def test_forms(self):
        form_data = {'something': 'something'}#to change
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        ... # other tests relating forms, for example checking the form data