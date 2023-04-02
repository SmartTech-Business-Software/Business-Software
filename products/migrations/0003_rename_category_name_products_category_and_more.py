# Generated by Django 4.1.3 on 2023-01-27 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='total_number_of_product',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='products',
            name='cat',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]