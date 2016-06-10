# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoice', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvoiceAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit', models.CharField(blank=True, default='', help_text="Clave Única de Identificación Tributaria means Unique Code of Tributary Identification. Everybody who isn't an employee under somebody's payroll has one. Even companies, NGOs, Fundations, etc.", max_length=14, verbose_name='CUIT')),
                ('iibb', models.CharField(blank=True, default='', help_text="Ingresos Brutos means gross revenue. It is a unique code given by fiscal regulators of provinces'.", max_length=15, verbose_name='IIBB')),
                ('invoice_company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.CompanyInvoice', verbose_name='company')),
            ],
            options={
                'verbose_name': 'company',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='ConceptType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
                ('code', models.SlugField(max_length=15, unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'concept type',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'concept types',
            },
        ),
        migrations.CreateModel(
            name='ContactInvoiceAR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(blank=True, choices=[('D', 'DNI'), ('T', 'CUIT'), ('L', 'CUIL')], max_length=1, null=True, verbose_name='id type')),
                ('id_number', models.CharField(blank=True, default='', max_length=14, verbose_name='id number')),
                ('invoice_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='invoice.ContactInvoice', verbose_name='contact')),
            ],
            options={
                'verbose_name': 'contact',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='InvoiceAR',
            fields=[
                ('invoice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoice.Invoice')),
                ('due_date', models.DateField(verbose_name='due date')),
                ('service_start', models.DateField(verbose_name='service start')),
                ('vat_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='VAT total')),
                ('concept_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice_ar.ConceptType', verbose_name='concept type')),
                ('invoicear_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice_ar.CompanyInvoiceAR', verbose_name='company AR')),
                ('invoicear_contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', related_query_name='invoice', to='invoice_ar.ContactInvoiceAR', verbose_name='contact AR')),
            ],
            options={
                'verbose_name': 'invoice',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'invoice',
            },
            bases=('invoice.invoice',),
        ),
        migrations.CreateModel(
            name='InvoiceARHasVATSubtotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='subtotal')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', related_query_name='+', to='invoice.VAT', verbose_name='VAT')),
            ],
            options={
                'verbose_name': 'VAT subtotal',
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'VAT subtotals',
            },
        ),
        migrations.CreateModel(
            name='PointOfSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afip_id', models.PositiveSmallIntegerField(verbose_name='AFIP id')),
                ('point_of_sale_type', models.CharField(choices=[('C', 'Fiscal Controller'), ('F', 'Pre-printed'), ('W', 'Webservice'), ('L', 'Online')], default='W', max_length=1, verbose_name='point of sale type')),
                ('is_inactive', models.BooleanField(default=False, verbose_name='is inactive')),
                ('fiscal_address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='point_of_sales', related_query_name='point_of_sale', to='persons.PhysicalAddress', verbose_name='fiscal address')),
                ('invoicear_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_of_sales', related_query_name='point_of_sale', to='invoice_ar.CompanyInvoiceAR', verbose_name='company')),
            ],
            options={
                'verbose_name': 'point of sale',
                'verbose_name_plural': 'point of sales',
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.AddField(
            model_name='invoicear',
            name='point_of_sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices_ar', related_query_name='invoice_ar', to='invoice_ar.PointOfSale', verbose_name='point of sale'),
        ),
        migrations.AddField(
            model_name='invoicear',
            name='vat_subtotals',
            field=models.ManyToManyField(related_name='_invoicear_vat_subtotals_+', related_query_name='invoicear', to='invoice_ar.InvoiceARHasVATSubtotal', verbose_name='VAT subtotals'),
        ),
        migrations.AlterUniqueTogether(
            name='pointofsale',
            unique_together=set([('invoicear_company', 'afip_id')]),
        ),
    ]
