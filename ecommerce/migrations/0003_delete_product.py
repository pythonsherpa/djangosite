# Generated by Django 4.1.1 on 2022-09-13 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0002_product_alter_customer_email_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Product",
        ),
    ]
