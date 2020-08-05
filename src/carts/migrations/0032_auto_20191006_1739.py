# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-06 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0031_auto_20190908_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total1',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
