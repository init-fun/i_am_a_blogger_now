from django.shortcuts import render, get_object_or_404, redirect
from .models import Product  # this is our products model
from .forms import ProductForm

# method to create a new product
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form,
    }
    return render(request, "products/product_create.html", context)


# product update view
def product_update_view(request, id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)


def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    print(f"this is the {obj}")
    print(request.method)
    if request.method == "POST":
        # user confirms that we want to delete something
        print("obj deleted")
        obj.delete()
        return redirect("../../")
    context = {"obj": obj}
    return render(request, "products/product_delete.html", context)


# ===============================================================

# def render_initial_data(request):
#     initial_data = {
#         "title": "default title",
#     }
#     obj = Product.objects.get(id=1)
#     form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {"form": form}
#     return render(request, "products/product_create.html", context)


# def dynamic_update_view(request, id):
#     obj = get_object_or_404(Product, id=id)
#     form = ProductForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         "form": form,
#     }
#     return render(request, "products/product_update.html", context)


# this is the code for our raw product form


# def product_create_view(request):
#     my_raw_form = RawProductForm()
#     if request.method == "POST":
#         my_raw_form = RawProductForm(request.POST)
#         if my_raw_form.is_valid():
#             print(my_raw_form.cleaned_data)
#             Product.objects.create(**my_raw_form.cleaned_data)
#     else:
#         my_raw_form = RawProductForm()

#     context = {
#         "my_raw_form": my_raw_form,
#     }
#     return render(request, "products/product_create.html", context)
