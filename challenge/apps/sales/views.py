import operator

from functools import reduce
from challenge.apps.sales.forms import FileSaleForm
from challenge.apps.sales.models import Sale
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class IndexSales(View):
    def get(self, request):
        sale_file = FileSaleForm()
        sales = Sale.objects.all()

        gross_sales = reduce(operator.add, [s.total_price for s in sales])

        return render(request, 'sales/index.html', {
            'gross_sales': gross_sales,
            'form': sale_file
        })


class NewSalesFile(View):
    def post(self, request, *args, **kwargs):
        form = FileSaleForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['sales_file']
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
                    )
            return HttpResponseRedirect('/sales/')
        else:
            return HttpResponse('error')
