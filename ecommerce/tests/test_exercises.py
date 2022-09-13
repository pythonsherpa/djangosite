from django.test import TestCase
from django.test import tag
from django.urls import reverse

from ecommerce.forms import ProductForm
from ecommerce.models import Product


class URLsTest(TestCase):

    @tag("to be implemented")
    def test_link_to_homepage(self):
        response = self.client.get("/ecommerce/customers/")
        homepage_url = reverse("home")
        self.assertContains(response, f'<a href="{homepage_url}">')

    @tag("to be implemented")
    def test_about_us(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)


class ProductTest(TestCase):
    @tag("to be implemented")
    def test_product_model(self):
        product = Product.objects.create(
            name="TV", price=999, description="55 inch QLED TV")
        assert product

    @tag("to be implemented")
    def test_product_list(self):
        """The URL for the list of all the products"""
        response = self.client.get("/ecommerce/products/")
        self.assertEqual(response.status_code, 200)

    @tag("to be implemented")
    def test_product_detail(self):
        """The URL for the detail page for a single product"""
        product = Product.objects.create(
            name="Tesla Model S",
            price=100000,
            description="Electric car",
        )
        response = self.client.get(f"/ecommerce/products/{product.id}")
        self.assertEqual(response.status_code, 200)

    @tag("to be implemented")
    def test_product_add(self):
        """The URL for adding a new product"""
        response = self.client.get("/ecommerce/products/add/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Add customer</h1>", html=True)


class ProductFormTest(TestCase):
    @tag("to be implemented")
    def test_product_form(self):
        form_data = {"name": "Cheese", "price": 5, "description": "From Dutch cows"}
        form = ProductForm(form_data)
        self.assertTrue(form.is_valid())
