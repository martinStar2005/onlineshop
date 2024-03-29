from django.test import TestCase
from django.shortcuts import reverse


class PagesTest(TestCase):
    def test_home_page_by_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_by_url(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'pages/about.html')

    def test_text_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home page')

    def test_text_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'About page')


