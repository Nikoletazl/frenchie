from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from frenchie.auth_app.models import Customer


class CustomerTest(TestCase):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(username='testuser', password='12345')

    VALID_CUSTOMER_DATA = {
        'name': 'Test',
        'email': 'test@test.it',
        'user': user,
    }

    def test_name_min_length(self):
        name = 'a'

        customer = Customer(
            name=name,
            email=self.VALID_CUSTOMER_DATA['email'],
            user=self.VALID_CUSTOMER_DATA['user'],
        )

        with self.assertRaises(ValidationError) as context:
            customer.full_clean()
            customer.save()

        self.assertIsNotNone(context.exception)
