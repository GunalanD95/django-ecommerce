# Generated by Django 4.0 on 2022-02-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esite', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
