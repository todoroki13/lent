# Generated by Django 3.2.7 on 2021-12-11 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_alter_logitems_itemtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logborrow',
            name='borrowps',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.logperson', verbose_name='借用人'),
        ),
        migrations.AlterField(
            model_name='logborrow',
            name='borrowsl',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='log.logitems', verbose_name='設備編號'),
        ),
    ]
