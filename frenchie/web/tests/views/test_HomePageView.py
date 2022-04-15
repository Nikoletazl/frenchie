from django.test import TestCase
from django.urls import resolve

from frenchie.web.views import HomePageView


class TestHomePageView(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.url_name, 'home page')