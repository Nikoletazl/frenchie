from django.test import TestCase
from django.urls import reverse


class CheckoutView(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('checkout'))

        self.assertTemplateUsed(response, 'store/checkout.html')