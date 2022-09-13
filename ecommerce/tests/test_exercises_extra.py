from django.test import TestCase, tag

from ecommerce.models import Customer


class ExtraExercisesTest(TestCase):
    @tag("to be implemented")
    def test_product_add(self):
        """The URL for adding a new product"""
        response = self.client.get("/ecommerce/products/add/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Add customer</h1>", html=True)

    @tag("to be implemented")
    def test_magic_method_str(self):
        """Pretty printing of a customer object"""
        c = Customer.objects.create(
            first_name="Albert", last_name="Einstein", email="albert@einstein.org"
        )
        self.assertTrue(isinstance(c, Customer))
        self.assertEqual(c.__str__(), "Albert Einstein")

