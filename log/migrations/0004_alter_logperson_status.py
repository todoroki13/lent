# Generated by Django 3.2.7 on 2021-12-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20211205_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logperson',
            name='status',
            field=models.IntegerField(choices=[(0, '行政人員'), (1, '正式教師'), (2, '代理教師'), (3, '兼任教師')], default=0, verbose_name='在校身分'),
        ),
    ]