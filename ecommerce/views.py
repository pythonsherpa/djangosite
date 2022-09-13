from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from ecommerce.forms import ContactForm, CustomerForm
from ecommerce.models import Customer


def index(request):
    return render(request, "ecommerce/index.html")


class CustomerListView(ListView):
    model = Customer
    template_name = "ecommerce/customer_list.html"


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "ecommerce/customer_detail.html"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = "/ecommerce/customers/"
    template_name = "ecommerce/customer_form.html"


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        context = {"form": form}
        return render(request, "contact.html", context)

    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            self.send_mail(form.cleaned_data)
            return HttpResponse("Thanks for your message")
        return render(request, "contact.html", {"form": form})

    def send_mail(self, valid_data):
        # Send mail logic
        pass
