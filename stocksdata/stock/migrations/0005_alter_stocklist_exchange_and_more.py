# Generated by Django 4.2.4 on 2023-10-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_stocklist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='exchange',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stocklist',
            name='exchange_short_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stocklist',
            name='stock_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]