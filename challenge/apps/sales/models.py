from django.db import models


class Document(models.Model):
    """
        Class representing the block of sales, originating from file.
        This class is util for grouping sales by file
    """
    created_date = models.DateTimeField(auto_now_add=True)
    parse_complete = models.NullBooleanField(default=False)

    def __str__(self):
        return 'Sale: {}'.format(self.id)


class Sale(models.Model):
    """
        Class representing each sale of Document (file containing the sale's
        information)
    """
    purchaser_name = models.CharField('Purchaser name', max_length=50)
    item_description = models.CharField('Item description', max_length=50)
    item_price = models.FloatField('Item price')
    purchase_count = models.IntegerField('Purcharse count')
    merchant_address = models.CharField('Merchart address', max_length=50)
    merchant_name = models.CharField('Nerchant name', max_length=50)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)

    @property
    def total_price(self):
        return self.item_price * self.purchase_count

    def __repr__(self):
        return 'Sale: {}'.format(self.id)

    def __str__(self):
        return 'Sale: {}'.format(self.id)
