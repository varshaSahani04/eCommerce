# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-12 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0042_auto_20190612_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
