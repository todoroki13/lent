# Generated by Django 3.2.7 on 2021-12-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0009_auto_20211212_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logborrow',
            name='borrowdt',
            field=models.DateField(auto_now_add=True, verbose_name='εεΊζι'),
        ),
    ]
