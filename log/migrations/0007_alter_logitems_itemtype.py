# Generated by Django 3.2.7 on 2021-12-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_alter_logborrow_borrowdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logitems',
            name='itemtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.logtype', verbose_name='客户'),
        ),
    ]
