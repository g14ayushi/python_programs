# Generated by Django 5.0.6 on 2024-06-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
