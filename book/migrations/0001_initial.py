# Generated by Django 2.0 on 2020-04-25 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('ISBN', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.IntegerField()),
                ('date', models.DateField()),
                ('username', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=20)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCrudentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=5)),
                ('company', models.CharField(max_length=20)),
                ('salt', models.CharField(max_length=32)),
                ('date_joined', models.DateField(default=datetime.date(2020, 4, 24))),
            ],
        ),
    ]
