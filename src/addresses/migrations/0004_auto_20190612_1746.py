# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-12 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_auto_20190525_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='Airoli', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='INDIA', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(default=400708, max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(default='maharastra', max_length=120),
        ),
    ]
