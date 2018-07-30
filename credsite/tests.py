from django.test import TestCase
from django.urls import reverse
from .models import Company


class CompanyModelTest(TestCase):

    def setUp(self):
        Company.objects.create(name='Virgin Hyperloop One',
                               description='we build hyperloops in CA',
                               brief_description='we build hyperloops')

    def test_text_content(self):
        company=Company.objects.get(id=1)
        expected_object_name = f'{company.name}'
        self.assertEqual(expected_object_name, 'Virgin Hyperloop One')


class HomePageViewTest(TestCase):

    def setUp(self):
        Company.objects.create(name='Virgin Hyperloop One',
                               description='we build hyperloops in CA',
                               brief_description='we build hyperloops')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
