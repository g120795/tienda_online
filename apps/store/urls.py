from django.urls import path
from .views import create_product
from .views import create_category
from .views import create_order
from .views import catalog
from .views import detail_product
urlpatterns = [
    #product
    path('create_product/', create_product, name='create_product'),
    path('catalog/', catalog, name='catalog'),
    path('<int:product_id>/detail_product/', detail_product, name='detail_product'),
    #category
    path('create_category/', create_category, name='create_category'),

    #order
    path('create_order/', create_order, name='create_order'),

]