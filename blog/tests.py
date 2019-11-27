from django.test import TestCase
from django.urls import reverse
from blog.models import Article, Categorie
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

class ArticleModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        categorie_test = Categorie.objects.create(nom='categorie_test')
        Article.objects.create(titre='titre_test', auteur='auteur_test', contenu='contenu_test', categorie=categorie_test)

    def test_titre_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('titre').verbose_name
        self.assertEquals(field_label, 'titre')

    def test_date_de_parution_label(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'Date de parution')

    def test_default_date_de_parution_label(self):
        article = Article.objects.get(id=1)
        date = article._meta.get_field('date').default
        self.assertEquals(date, timezone.now)


class BlogViewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        number_of_articles = 10
        categorie_test = Categorie.objects.create(nom='categorie_test')
        img = SimpleUploadedFile(name='test_image.jpg', content=open('static/images/logo.png', 'rb').read(), content_type='image/png')

        for article_id in range(number_of_articles):
            Article.objects.create(
                titre=f'Article_test {article_id}',
                auteur=f'Auteur_test {article_id}',
                contenu=f'Contenu test {article_id}',
                slug=f'slug-{article_id}',
                categorie=categorie_test,
                photo=img
            )

# List view      
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)   
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogList.html')
        
    def test_pagination_is_four(self):
        response = self.client.get(reverse('blogList'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['list_articles']) == 4)

    def test_lists_all_articles(self):
        response = self.client.get(reverse('blogList')+'?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['list_articles']) == 2)

    def test_404_not_found(self):
        response = self.client.get(reverse('blogList')+'wrongpath')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

# Blog details view
    def test_detailsview_uses_correct_template(self):
        response = self.client.get('/blog/blogDetails/2-slug-0')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogDetails.html')

    def test_details_404_not_found(self):
        response = self.client.get('/blog/blogDetails/2-slug-2')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

#Category view
    def test_category_view_uses_correct_template(self):
        response = self.client.get('/blog/category/categorie_test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogList.html')

    def test_lists_all_articles_by_category(self):
        response = self.client.get('/blog/category/categorie_test')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['list_articles']) == 4)
