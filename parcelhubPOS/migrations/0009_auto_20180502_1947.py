# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-02 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcelhubPOS', '0008_auto_20180429_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='totalgst',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Total GST'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Total price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='unit',
            field=models.IntegerField(default=1),
        ),
    ]
