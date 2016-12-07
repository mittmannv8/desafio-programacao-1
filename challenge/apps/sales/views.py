import operator

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from functools import reduce

from challenge.apps.sales.models import Document
from challenge.apps.sales.models import Sale


class IndexSales(View):
    def get(self, request):
        """
            Return and template containing the last document sales (if exist)
            and sum of all sales.
        """
        sales = Sale.objects.all()
        last_document = Document.objects.last() or None

        if not last_document:
            last_gross_sales = 0
            gross_sales = 0
        else:
            last_sales = sales.filter(document=last_document)
            last_gross_sales = reduce(
                operator.add,
                [s.total_price for s in last_sales]
            )
            gross_sales = reduce(operator.add, [s.total_price for s in sales])

        return render(request, 'sales/index.html', {
            'gross_sales': gross_sales,
            'last_gross_sales': last_gross_sales,
            'last_document': last_document,
        })


class NewSalesFile(View):
    def post(self, request, *args, **kwargs):
        """
            Receive a file, parse and save the data on DB.
        """
        try:
            file = request.FILES['sales_file']

            document = Document.objects.create()

            for index, line in enumerate(file.readlines()):
                line = line.decode('utf-8')
                values = line.split('\t')

                if index > 0:
                    Sale.objects.create(
                       purchaser_name=values[0],
                       item_description=values[1],
                       item_price=float(values[2]),
                       purchase_count=int(values[3]),
                       merchant_address=values[4],
                       merchant_name=values[5],
                       document=document
                    )
            document.parse_complete = True
            document.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Documento inserido com sucesso'
            )
        except:
            document.delete()
            messages.add_message(
                request,
                messages.ERROR,
                'Houve um erro ao inserir o documento. Tente novamente mais tarde.'
            )
        return HttpResponseRedirect('/')
