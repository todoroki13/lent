# Generated by Django 3.2.7 on 2021-12-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20211212_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logborrow',
            name='borrowdt',
            field=models.DateField(verbose_name='借出時間'),
        ),
    ]
