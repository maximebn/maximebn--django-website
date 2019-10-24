from django.test import TestCase
from contact.forms import MyForm

class MyTests(TestCase):
    
    def test_forms(self):
        form_data = {'something': 'something'}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())
        ... # other tests relating forms, for example checking the form data