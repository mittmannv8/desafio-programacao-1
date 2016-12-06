from django.test import TestCase
from challenge.apps.sales.models import Sale


class SaleTestCase(TestCase):

    def setUp(self):
        Sale.objects.create(
           purchaser_name='Purchaser',
           item_description='Description',
           item_price=1.99,
           purchase_count=2,
           merchant_address='Address',
           merchant_name='Merchant'
        )

    def tests_sales_models(self):
        sale = Sale.objects.get(id=1)
        print(sale)
        self.assertEqual(sale.purchaser_name, 'Purchaser')
        self.assertEqual(sale.item_description, 'Description')
        self.assertEqual(sale.merchant_address, 'Address')
        self.assertEqual(sale.merchant_name, 'Merchant')
        self.assertEqual(sale.total_price, 3.98)
