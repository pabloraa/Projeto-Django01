from django.urls import path

from .views import index,contato,sobre, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre),
    path('produto/<int:pk>', produto, name='produto'),
]