# Generated by Django 3.2.2 on 2021-05-12 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
            options={
                'db_table': 'productimages',
            },
        ),
        migrations.RenameModel(
            old_name='Product_Size',
            new_name='ProductSize',
        ),
        migrations.RenameModel(
            old_name='Theme_Product',
            new_name='ThemeProduct',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_img',
        ),
        migrations.RemoveField(
            model_name='size',
            name='product',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='description_iamge_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='products',
            field=models.ManyToManyField(through='products.ProductSize', to='products.Product'),
        ),
        migrations.AddField(
            model_name='theme',
            name='products',
            field=models.ManyToManyField(through='products.ThemeProduct', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='productsize',
            table='productssizes',
        ),
        migrations.AlterModelTable(
            name='themeproduct',
            table='themesproducts',
        ),
        migrations.DeleteModel(
            name='Product_Image',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
