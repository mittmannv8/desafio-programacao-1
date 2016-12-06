from __future__ import unicode_literals

from django.db import models


class Sale(models.Model):
    purchaser_name = models.CharField('Purchaser name', max_length=50)
    item_description = models.CharField('Item description', max_length=50)
    item_price = models.FloatField('Item price')
    purchase_count = models.IntegerField('Purcharse count')
    merchant_address = models.CharField('Merchart address', max_length=50)
    merchant_name = models.CharField('Nerchant name', max_length=50)

    @property
    def total_price(self):
        return self.item_price * self.purchase_count

    def __repr__(self):
        return 'Sale: {}'.format(self.id)
