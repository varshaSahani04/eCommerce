# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-21 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0013_auto_20190521_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='updated',
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]