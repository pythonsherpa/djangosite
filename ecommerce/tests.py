from django.test import Client, TestCase

from ecommerce.forms import ContactForm


class IndexTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index1(self):
        # Issue a GET request.
        response = self.client.get('/ecommerce/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_index2(self):
        response = self.client.get('/ecommerce/index2')
        self.assertEqual(response.status_code, 200)

    def test_index3(self):
        response = self.client.get('/ecommerce/index2')
        self.assertEqual(response.status_code, 200)


class CustomerFormTest(TestCase):
    pass


class ContactFormTest(TestCase):

    def test_contact_form_renders(self):
        form = ContactForm()
        self.assertInHTML(
            '<input type="text" name="name" required id="id_name">',
            str(form)
        )
