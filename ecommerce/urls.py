from django.urls import path

from ecommerce import views

urlpatterns = [
    path("customers/", views.CustomerListView.as_view(), name="customer-list"),
    path("customers/<int:pk>", views.CustomerDetailView.as_view(), name="customer-detail"),
    path("customers/add/", views.CustomerCreateView.as_view(), name="customer-add"),

    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/add/", views.ProductCreateView.as_view(), name="product-add"),
]
