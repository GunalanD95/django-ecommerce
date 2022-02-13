# Generated by Django 4.0 on 2022-02-13 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esite', '0009_productvariant_product_product_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='esite.productcategory'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='size',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='variant',
            field=models.CharField(max_length=200, null=True),
        ),
    ]