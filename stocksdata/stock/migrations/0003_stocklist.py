# Generated by Django 4.2.4 on 2023-10-31 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_delete_stocklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('exchange', models.CharField(max_length=50)),
                ('exchange_short_name', models.CharField(max_length=20)),
                ('stock_type', models.CharField(max_length=20)),
            ],
        ),
    ]
