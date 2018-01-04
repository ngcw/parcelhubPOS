# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0014_auto_20180104_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='gst',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='*GST(%)'),
        ),
    ]