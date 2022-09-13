from django import forms
from django.utils.translation import gettext_lazy as _

from ecommerce.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': "johndoe@hotmail.com"})
        }


class ProductForm(forms.ModelForm):
    # TODO: create a form for products
    pass


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
