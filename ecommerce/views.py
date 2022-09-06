from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView

from ecommerce.forms import ContactForm
from ecommerce.models import Customer


def index(request):
    return HttpResponse("Welcome at the ecommerce homepage.")


class IndexView(View):
    def get(self, request):
        return HttpResponse("Welcome at the ecommerce Class Based View homepage.")


class IndexTemplateView(TemplateView):
    template_name = "ecommerce/index.html"


def contact_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


class CustomerListView(ListView):
    model = Customer
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("customer-list")
