from django.db import transaction
from django.test import TestCase

from .models import Item, Log


class ItemTestCase(TestCase):
    def test_signals_run_in_same_transaction(self):
        # Start a transaction
        with transaction.atomic():
            # Create an Item
            item = Item.objects.create(name='Test Item')

            # Check if log entry was created within the transaction
            log_entry = Log.objects.first()
            self.assertIsNotNone(log_entry)
            self.assertEqual(log_entry.message, 'Item "Test Item" created.')

            # Rollback the transaction
            transaction.set_rollback(True)

        # Outside the atomic block, verify the log entry is gone
        self.assertEqual(Log.objects.count(), 0)
