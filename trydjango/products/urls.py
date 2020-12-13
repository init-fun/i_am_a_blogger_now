from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

app_name = "products"
urlpatterns = [
    # list all products
    path("", product_list_view, name="product_list"),
    # get a particular product detail
    path("<int:id>/", product_detail_view, name="product_detail_view"),
    # create a new product
    path("create/", product_create_view, name="product_create_view"),
    # update a object
    path("<int:id>/update/", product_update_view, name="product_update_view"),
    # delete a particular object
    path("<int:id>/delete/", product_delete_view, name="product_delete_view"),
    # path("products/", product_detail_view, name="product_detail_view"),
]