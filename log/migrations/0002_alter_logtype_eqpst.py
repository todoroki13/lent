# Generated by Django 3.2.7 on 2021-12-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtype',
            name='eqpst',
            field=models.IntegerField(choices=[(0, '使用中'), (1, '已淘汰')], default=0, verbose_name='設備狀態'),
        ),
    ]
