# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0023_school_general_information_other_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_core_values',
            name='core_value_ten',
            field=models.CharField(max_length=300, null=True),
        ),
    ]