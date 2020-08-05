# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-25 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_auto_20190524_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address_line2',
            new_name='address_line_2',
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='United States of America', max_length=120),
        ),
    ]