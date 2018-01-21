# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-21 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0002_auto_20180121_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cashupreportpaymenttype',
            old_name='repordid',
            new_name='cashupreport',
        ),
        migrations.AddField(
            model_name='terminal',
            name='float',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='cashupreport',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
    ]