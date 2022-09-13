from django import forms

from ecommerce.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': "johndoe@hotmail.com"}),
            'notes': forms.Textarea(attrs={'cols': 40, 'rows': 5})
        }


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
