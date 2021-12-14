# Generated by Django 3.2.7 on 2021-12-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowdt', models.DateField(verbose_name='購買時間')),
                ('backdt', models.DateField(blank=True, null=True, verbose_name='歸還日期')),
            ],
        ),
        migrations.CreateModel(
            name='LogItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=63, verbose_name='設備編號')),
                ('tenure', models.CharField(max_length=63, verbose_name='財產編號')),
                ('remark', models.TextField(max_length=511, verbose_name='備註')),
            ],
        ),
        migrations.CreateModel(
            name='LogPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='借用人')),
                ('status', models.IntegerField(choices=[(0, '行政人員'), (1, '正式教師'), (2, '代理教師'), (3, '兼任教師')], default=0, verbose_name='處理進度')),
                ('department', models.IntegerField(choices=[(0, '高中部'), (1, '國中部')], default=0, verbose_name='國/高中部')),
                ('title', models.CharField(max_length=255, verbose_name='科目/行政職稱')),
                ('phone', models.CharField(max_length=30, verbose_name='聯絡電話')),
                ('mail', models.EmailField(max_length=255, verbose_name='電子信箱')),
                ('isatwork', models.IntegerField(choices=[(0, '工作中'), (1, '已離職')], default=0, verbose_name='在職狀態')),
            ],
        ),
        migrations.CreateModel(
            name='LogType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=63, verbose_name='型號')),
                ('buydate', models.DateField(verbose_name='購買時間')),
                ('detail', models.TextField(max_length=511, verbose_name='詳細規格')),
                ('eqpst', models.IntegerField(choices=[(0, '行政人員'), (1, '正式教師'), (2, '代理教師'), (3, '兼任教師')], default=0, verbose_name='設備狀態')),
            ],
        ),
    ]