from challenge.apps.sales.forms import FileSaleForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from challenge.apps.sales.models import Sale


class SalesFileView(View):
    def get(self, request, *args, **kwargs):
        form = FileSaleForm()
        return render(request, 'sales/sales_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = FileSaleForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['sales_file']
            for index, line in enumerate(file.readlines()):
                line = line.decode('utf-8')
                values = line.split('\t')
                print(values[0])
                if index > 0:
                    Sale.objects.create(
                       purchaser_name=values[0],
                       item_description=values[1],
                       item_price=float(values[2]),
                       purchase_count=int(values[3]),
                       merchant_address=values[4],
                       merchant_name=values[5],
                    )
            return HttpResponse('OK')
        else:
            return HttpResponse('error')
