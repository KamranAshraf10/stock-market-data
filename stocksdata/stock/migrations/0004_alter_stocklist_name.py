# Generated by Django 4.2.4 on 2023-10-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_stocklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklist',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]