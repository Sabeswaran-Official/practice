from django.urls import path
from .views import *

urlpatterns = [
    # path('products/add/', ProductsAdd),
    # path('products/', AllProducts),
    # path('products/delete/<int:id>/', DeleteProducts, name='product_delete'),  
    # path('products/update/<int:id>/', ProductUpdate, name='product_update'),  

    path('products/add/', ProductsAddView.as_view()),
    path('products/', ProductsListView.as_view()),
    path('products/delete/<int:id>/', ProductDeleteView.as_view(), name='product_delete'),  
    path('products/update/<int:id>/', ProductUpdateView.as_view(), name='product_update'),  
]