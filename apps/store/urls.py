from django.urls import path
from .views import create_product
from .views import create_category
from .views import create_order
from .views import catalog
from .views import detail_product
from .views import add_to_cart
from .views import cart
from .views import pay_method
from .views import payment
from .views import update_product
from .views import list_order
from .views import seller_catalog
from .views import seller_detail_product
from .views import delete_product
from .views import mi_orders

urlpatterns = [
    #product
    path('create_product/', create_product, name='create_product'),
    path('catalog/', catalog, name='catalog'),
    path('seller_catalog/', seller_catalog, name='seller_catalog'),
    path('<int:product_id>/seller_detail_product/', seller_detail_product, name='seller_detail_product'),
    path('<int:product_id>/detail_product/', detail_product, name='detail_product'),
    path('<int:product_id>/update_product/', update_product, name='update_product'),
    path('<int:product_id>/delete_product/', delete_product, name='delete_product'),
    
    #category
    path('create_category/', create_category, name='create_category'),

    #order
    path('create_order/', create_order, name='create_order'),
    path('<int:product_id>/compra', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('pay_method', pay_method, name='pay_method' ),
    path('payment/', payment, name='payment'),
    path('list_order/', list_order, name='list_order'),
    path('mi_orders/', mi_orders, name='mi_orders')

]