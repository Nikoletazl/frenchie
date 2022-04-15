import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from frenchie.web.models import Order


class OrderModelTest(TestCase):
    VALID_ORDER_DATA = {
        'date_ordered': datetime.datetime.now(),
        'complete': False,
        'transaction_id': 12345678999,
    }

    def test_if_transaction_id_is_less_than_10(self):
        transaction_id = 123456789

        order = Order(
            date_ordered=self.VALID_ORDER_DATA['date_ordered'],
            transaction_id=transaction_id,
            complete=self.VALID_ORDER_DATA['complete'],
        )

        with self.assertRaises(ValidationError) as context:
            order.full_clean()
            order.save()

        self.assertIsNotNone(context.exception)