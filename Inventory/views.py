from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# def ProductsAdd(request):

#     context = {
#         'product_form': Product_Form()
#     }

#     if request.method == "POST":

#         product_form = Product_Form(request.POST)

#         if product_form.is_valid():

#             product_form.save()

#             return redirect('/inventory/products/')

#     return render(request, 'products_add.html', context)

# def AllProducts(request):

#     context = {
#       "all_products": Product.objects.all()
#     }

#     return render(request, 'products.html', context)

# def DeleteProducts(request, id):

#     selected_product = Product.objects.get(id = id)

#     selected_product.delete()

#     return redirect('/inventory/products/')

# def ProductUpdate(request, id):

#     selected_product = Product.objects.get(id = id)

#     context = {
#         "product_form" : Product_Form(instance=selected_product)
#     }

#     if request.method == 'POST':

#         product_form = Product_Form(request.POST, instance=selected_product)

#         if product_form.is_valid():

#             product_form.save()

#             return redirect('/inventory/products/')

#     return render(request, 'products_add.html', context)


class ProductsAddView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request):

        context = {
            'product_form': Product_Form()
        }

        return render(request, 'products_add.html', context)

    def post(self, request):

        print("from class based post")

        product_form = Product_Form(request.POST, request.FILES)

        if product_form.is_valid():

            product_form.save()

            return redirect('/inventory/products/')
        
class ProductsListView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request):

        context = {
        "all_products": Product.objects.all()
        }

        return render(request, 'products.html', context)
    
class ProductDeleteView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request, id):

        selected_product = Product.objects.get(id = id)

        selected_product.delete()

        return redirect('/inventory/products/')


class ProductUpdateView(LoginRequiredMixin, View):

    login_url = '/'

    def get(self, request, id):

        selected_product = Product.objects.get(id = id)

        context = {
            "product_form" : Product_Form(instance=selected_product)
        }

        return render(request, 'products_add.html', context)

    def post(self, request, id):

        selected_product = Product.objects.get(id = id)

        product_form = Product_Form(request.POST, instance=selected_product)

        if product_form.is_valid():

            product_form.save()

            return redirect('/inventory/products/')