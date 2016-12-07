from django.conf.urls import url
from challenge.apps.sales import views


urlpatterns = [
    url(r'^$', views.IndexSales.as_view(), name='sale_index'),
    url(r'^new/$', views.NewSalesFile.as_view(), name='new_sale'),
]
