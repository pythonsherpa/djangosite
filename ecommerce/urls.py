from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    path('index2', views.IndexView.as_view(), name='index2'),
    path('index3', views.IndexTemplateView.as_view(), name='index3'),

    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', views.CustomerCreateView.as_view(), name='customer-add'),
]
