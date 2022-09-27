from django import forms

from ecommerce.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': "johndoe@hotmail.com"})
        }


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
