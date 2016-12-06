from django import forms


class FileSaleForm(forms.Form):
    sales_file = forms.FileField('File')
