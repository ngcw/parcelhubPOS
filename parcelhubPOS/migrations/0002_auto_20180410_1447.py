# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-10 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashupreport',
            name='terminal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Terminal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoice',
            name='terminal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Terminal'),
            preserve_default=False,
        ),
    ]
