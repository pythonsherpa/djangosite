from django.test import Client, TestCase

from ecommerce.models import Customer


class ViewsTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home(self):
        # Issue a GET request.
        response = self.client.get("/")
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_customer_list(self):
        response = self.client.get("/ecommerce/customers/")
        self.assertEqual(response.status_code, 200)

    def test_customer_detail(self):
        customer = Customer.objects.create(
            first_name="John", last_name="Doe", email="john@doe.com"
        )
        response = self.client.get(f"/ecommerce/customers/{customer.id}")
        self.assertEqual(response.status_code, 200)

    def test_customer_add_get_shows_form(self):
        response = self.client.get("/ecommerce/customers/add/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="ecommerce/customer_form.html")
        self.assertContains(response, "<h1>Add customer</h1>", html=True)

    def test_customer_add_post_creates_customer_in_database(self):
        self.client.post(
            "/ecommerce/customers/add/",
            data={"first_name": "Donald", "last_name": "Knuth", "email": "donald@knuth.com"},
        )
        self.assertEqual(Customer.objects.last().first_name, "Donald")
