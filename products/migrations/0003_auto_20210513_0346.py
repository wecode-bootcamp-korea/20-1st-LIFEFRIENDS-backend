# Generated by Django 3.2.2 on 2021-05-13 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210512_0513'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productimage',
            table='product_images',
        ),
        migrations.AlterModelTable(
            name='productsize',
            table='products_sizes',
        ),
        migrations.AlterModelTable(
            name='themeproduct',
            table='themes_products',
        ),
    ]