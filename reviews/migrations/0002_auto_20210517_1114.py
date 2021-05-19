# Generated by Django 3.2.2 on 2021-05-17 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.AddField(
            model_name='review',
            name='productsize',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productsize'),
        ),
    ]