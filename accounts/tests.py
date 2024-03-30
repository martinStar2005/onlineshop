from django.test import TestCase
from django.shortcuts import reverse
from .models import CustomUSer
from django.shortcuts import redirect
from django.contrib.auth import get_user_model


class AccountsTest(TestCase):
    username = 'matin'
    email = 'larsen.martin2005@gmail.com'

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='javad', email='larsen.martin2005@gmail.com', password='javad2005' )

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'javad',
                                                       'password': 'javad2005'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


    def test_signup(self):
        response = get_user_model().objects.create_user(
            self.username,
            self.email
        )

        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertEqual(get_user_model().objects.all()[1].username, 'matin')
        self.assertEqual(get_user_model().objects.all()[1].email, 'larsen.martin2005@gmail.com')


    def test_login_by_name(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'username')
        self.assertContains(response, 'password')

    def test_signup_by_name(self):
        response = self.client.get(reverse('signup'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'username')
        self.assertContains(response, 'email')
        self.assertContains(response, 'password')
