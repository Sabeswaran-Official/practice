# Generated by Django 4.2.14 on 2024-10-08 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.category'),
        ),
    ]
