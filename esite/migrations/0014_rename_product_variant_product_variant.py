# Generated by Django 4.0 on 2022-02-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esite', '0013_alter_productvariant_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_variant',
            new_name='variant',
        ),
    ]
