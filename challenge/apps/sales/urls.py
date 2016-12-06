from django.conf.urls import url
from challenge.apps.sales import views


urlpatterns = [
    url(r'^$', views.SalesFileView.as_view(), name='saleIndex'),
]
