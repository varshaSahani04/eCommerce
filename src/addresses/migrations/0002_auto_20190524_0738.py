# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-24 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adress',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='adress_line1',
            new_name='address_line1',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='adress_line2',
            new_name='address_line2',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='adress_type',
            new_name='address_type',
        ),
    ]
