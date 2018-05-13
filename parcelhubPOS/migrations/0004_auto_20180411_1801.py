# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-11 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0003_auto_20180410_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='terminal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Terminal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementofaccount',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch'),
        ),
    ]
