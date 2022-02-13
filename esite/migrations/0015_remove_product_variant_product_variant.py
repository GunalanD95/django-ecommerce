# Generated by Django 4.0 on 2022-02-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esite', '0014_rename_product_variant_product_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='variant',
        ),
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.ManyToManyField(blank=True, null=True, to='esite.ProductVariant'),
        ),
    ]
