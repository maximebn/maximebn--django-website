from django.test import TestCase
from django.urls import reverse

class AnnexesViewTests(TestCase):
    
# Mentions view      
    def test_mentions_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)   
        
    def test_mentions_view_uses_correct_template(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annexes/mentions.html')

    
# about view      
    def test_about_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)   
        
    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annexes/about.html')

# policy view      
    def test_policy_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('policy'))
        self.assertEqual(response.status_code, 200)   
        
    def test_policy_view_uses_correct_template(self):
        response = self.client.get(reverse('policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'annexes/policy.html')