# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 13:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogues', '0006_auto_20170830_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='School_anthem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stanza_one', models.TextField()),
                ('stanza_two', models.TextField()),
                ('stanza_three', models.TextField()),
                ('stanza_four', models.TextField()),
                ('stanza_five', models.TextField()),
                ('stanza_six', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School_core_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_value_one', models.CharField(max_length=300)),
                ('core_value_two', models.CharField(max_length=300)),
                ('core_value_three', models.CharField(max_length=300)),
                ('core_value_four', models.CharField(max_length=300)),
                ('core_value_five', models.CharField(max_length=300)),
                ('core_value_six', models.CharField(max_length=300)),
                ('core_value_seven', models.CharField(max_length=300)),
                ('core_value_eight', models.CharField(max_length=300)),
                ('core_value_nine', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School_rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_one', models.CharField(max_length=300)),
                ('rule_two', models.CharField(max_length=300)),
                ('rule_three', models.CharField(max_length=300)),
                ('rule_four', models.CharField(max_length=300)),
                ('rule_five', models.CharField(max_length=300)),
                ('rule_six', models.CharField(max_length=300)),
                ('rule_seven', models.CharField(max_length=300)),
                ('rule_eight', models.CharField(max_length=300)),
                ('rule_nine', models.CharField(max_length=300)),
                ('rule_ten', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='school_general_information',
            name='school_anthem',
        ),
        migrations.RemoveField(
            model_name='school_general_information',
            name='school_core_values',
        ),
        migrations.RemoveField(
            model_name='school_general_information',
            name='school_rules',
        ),
    ]