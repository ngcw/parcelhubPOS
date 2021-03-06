# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-13 16:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='*Name')),
                ('branch_code', models.CharField(max_length=10, verbose_name='*Branch code')),
                ('owner', models.CharField(max_length=50, verbose_name='*Owner')),
                ('contact', models.CharField(max_length=25, verbose_name='*Contact')),
                ('email', models.EmailField(max_length=254, verbose_name='*Email')),
                ('address', models.CharField(max_length=254, verbose_name='*Address')),
                ('registrationno', models.CharField(max_length=50, verbose_name='*Registration no')),
                ('gstno', models.CharField(max_length=50, verbose_name='*GST no')),
                ('fax', models.CharField(blank=True, max_length=25, null=True)),
                ('tollfree', models.CharField(blank=True, max_length=25, null=True, verbose_name='Toll-free')),
                ('website', models.CharField(blank=True, max_length=254, null=True)),
                ('payment_bank', models.CharField(blank=True, max_length=254, null=True)),
                ('payment_acc', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CashUpReport',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('sessiontimestamp', models.DateTimeField(verbose_name='session timestamp')),
                ('invoicenofrom', models.CharField(blank=True, max_length=100, null=True, verbose_name='Invoice from')),
                ('invoicenoto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Invoice to')),
                ('createtimestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create timestamp')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CashUpReportPaymentType',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=30)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=30)),
                ('count', models.IntegerField()),
                ('cashupreport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.CashUpReport')),
            ],
        ),
        migrations.CreateModel(
            name='CourierVendor',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='*Name')),
                ('formula', models.CharField(max_length=254, verbose_name='*Formula')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='*Name')),
                ('contact', models.CharField(max_length=25, verbose_name='*Contact')),
                ('fax', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='*Email')),
                ('identificationno', models.CharField(max_length=50, verbose_name='*Registration/IC No')),
                ('addressline1', models.CharField(blank=True, max_length=254, null=True, verbose_name='Address line 1')),
                ('addressline2', models.CharField(blank=True, max_length=254, null=True, verbose_name='line 2')),
                ('addressline3', models.CharField(blank=True, max_length=254, null=True, verbose_name='line 3')),
                ('addressline4', models.CharField(blank=True, max_length=254, null=True, verbose_name='line 4')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch', verbose_name='*Branch')),
            ],
            options={
                'ordering': ['branch', 'name'],
            },
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='*Name')),
                ('iscorporate', models.BooleanField()),
                ('iswalkinspecial', models.BooleanField()),
                ('iswalkin', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GlobalParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_lockin_date', models.DateField(verbose_name='*Invoice lock in date')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('invoiceno', models.CharField(max_length=25, verbose_name='Invoice No.')),
                ('remarks', models.CharField(blank=True, max_length=254, null=True)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=30)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('discountvalue', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Discount (RM)')),
                ('discountmode', models.CharField(blank=True, max_length=25, null=True, verbose_name='Discount mode')),
                ('gst', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='GST')),
                ('total', models.DecimalField(decimal_places=2, max_digits=30)),
                ('payment', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('createtimestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='*Invoice datetime')),
                ('updatetimestamp', models.DateTimeField(blank=True, null=True, verbose_name='Update datetime')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('tracking_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Track code')),
                ('skudescription', models.CharField(max_length=255, verbose_name='*Description')),
                ('zone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Zone')),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Weight(kg)')),
                ('dimension_weight', models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Dim wt(kg)')),
                ('height', models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Height(cm)')),
                ('length', models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Length(cm)')),
                ('width', models.DecimalField(blank=True, decimal_places=3, max_digits=25, null=True, verbose_name='Width(cm)')),
                ('sku', models.CharField(max_length=100, verbose_name='*SKU')),
                ('gst', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='GST')),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parcelhubPOS.CourierVendor')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='*Name')),
                ('iscustomer', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('createtimestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create timestamp')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Customer', verbose_name='*Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInvoice',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('remainder', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Remainder')),
                ('paidamount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=30, null=True, verbose_name='Paid amount')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Invoice')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='*Name')),
                ('legend', models.CharField(blank=True, max_length=5, null=True, verbose_name='*Legend')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='*Name')),
                ('isdocument', models.BooleanField()),
                ('ismerchandise', models.BooleanField()),
                ('default_courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.CourierVendor', verbose_name='Default courier')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_code', models.CharField(max_length=20, unique=True, verbose_name='*SKU')),
                ('description', models.CharField(max_length=254, verbose_name='*Description')),
                ('zone', models.IntegerField(blank=True, null=True, verbose_name='*Zone')),
                ('weight_start', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='*Weight start(kg)')),
                ('weight_end', models.DecimalField(blank=True, decimal_places=3, max_digits=30, null=True, verbose_name='*Weight end(kg)')),
                ('is_gst_inclusive', models.BooleanField(default=False, verbose_name='GST inclusive')),
                ('corporate_price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='*Corporate price')),
                ('walkin_special_price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='*Walk in special price')),
                ('walkin_price', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='*Walk in price')),
                ('updatetimestamp', models.DateTimeField(auto_now=True, verbose_name='master update time')),
                ('couriervendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.CourierVendor', verbose_name='*Courier')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ProductType', verbose_name='*Product type')),
            ],
            options={
                'ordering': ['sku_code'],
            },
        ),
        migrations.CreateModel(
            name='SKUBranch',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('corporate_override', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('walkin_special_override', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('walkin_override', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('updatetimestamp', models.DateTimeField(auto_now=True, verbose_name='last update timestamp')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch', verbose_name='*Branch')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parcelhubPOS.Customer')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.SKU', verbose_name='*SKU')),
            ],
        ),
        migrations.CreateModel(
            name='StatementOfAccount',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('datefrom', models.DateField(verbose_name='*Date from')),
                ('dateto', models.DateField(verbose_name='*Date to')),
                ('totalamount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Total amt')),
                ('paidamount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Paid amt')),
                ('outstandindamount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Outstanding amt')),
                ('createtimestamp', models.DateTimeField(verbose_name='create timestamp')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Customer', verbose_name='*Customer')),
            ],
        ),
        migrations.CreateModel(
            name='StatementOfAccountInvoice',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Invoice')),
                ('soa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.StatementOfAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='*Tax code')),
                ('gst', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='*GST(%)')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='*Name')),
                ('float', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('isactive', models.BooleanField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='UserBranchAccess',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('access_level', models.CharField(max_length=20, verbose_name='*Access level')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Branch', verbose_name='*Branch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='*User')),
            ],
        ),
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneDomestic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=25, verbose_name='*State')),
                ('postcode_start', models.CharField(max_length=25, verbose_name='*Postcode start')),
                ('postcode_end', models.CharField(max_length=25, verbose_name='*Postcode end')),
                ('zone', models.PositiveIntegerField(verbose_name='*Zone')),
            ],
            options={
                'ordering': ['zone'],
            },
        ),
        migrations.CreateModel(
            name='ZoneInternational',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, unique=True, verbose_name='*Country')),
                ('zone_doc', models.PositiveIntegerField(verbose_name='*Zone document')),
                ('zone_mer', models.PositiveIntegerField(verbose_name='*Zone merchandise')),
                ('couriervendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.CourierVendor', verbose_name='*Courier')),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='ZoneType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('isother', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='zonedomestic',
            unique_together=set([('state', 'postcode_start', 'postcode_end')]),
        ),
        migrations.AddField(
            model_name='sku',
            name='tax_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.Tax', verbose_name='*Tax code'),
        ),
        migrations.AddField(
            model_name='sku',
            name='zone_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ZoneType', verbose_name='*Zone type'),
        ),
        migrations.AddField(
            model_name='producttype',
            name='default_zonetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ZoneType', verbose_name='Default zone type'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_paymenttype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.PaymentType', verbose_name='Payment method'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='producttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ProductType', verbose_name='*Product type'),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='zone_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ZoneType', verbose_name='Zone type'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoicetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.InvoiceType', verbose_name='*Type'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.PaymentType'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.CustomerType', verbose_name='*Type'),
        ),
        migrations.AddField(
            model_name='couriervendor',
            name='zone_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.ZoneType', verbose_name='*Zone type'),
        ),
        migrations.AddField(
            model_name='cashupreportpaymenttype',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcelhubPOS.PaymentType'),
        ),
        migrations.AlterUniqueTogether(
            name='skubranch',
            unique_together=set([('sku', 'branch', 'customer')]),
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together=set([('branch', 'invoiceno')]),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('branch', 'identificationno')]),
        ),
    ]
