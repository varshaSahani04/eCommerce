# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-08 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0029_auto_20190908_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
