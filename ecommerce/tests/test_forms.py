from django.test import TestCase

from ecommerce.forms import ContactForm, CustomerForm


class CustomerFormTest(TestCase):
    def test_customer_form(self):
        form_data = {
            "first_name": "Jack",
            "last_name": "Daniels",
            "email": "jack@daniels.com",
        }
        form = CustomerForm(data=form_data)
        self.assertTrue(form.is_valid())


class ContactFormTest(TestCase):
    def test_contact_form_renders(self):
        form = ContactForm()
        self.assertInHTML(
            '<input type="text" name="name" required id="id_name">', str(form)
        )

    def test_contact_form_view_get(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_contact_form_view_post_renders(self):
        response = self.client.post("/contact/")
        self.assertEqual(response.status_code, 200)
