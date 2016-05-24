# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(verbose_name='code')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='balance')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'accounts',
                'verbose_name': 'account',
            },
        ),
        migrations.CreateModel(
            name='AccountSubtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_type', models.CharField(choices=[('P', 'Personal'), ('R', 'Real'), ('N', 'Nominal')], db_index=True, max_length=1, verbose_name='main type')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_subtypes', related_query_name='account_subtype', to='persons.Company', verbose_name='company')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'account subtypes',
                'verbose_name': 'account subtype',
            },
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledgers', related_query_name='ledger', to='persons.Company', verbose_name='company')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'ledgers',
                'verbose_name': 'ledger',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='amount')),
                ('debit_account_balance', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='account balance')),
                ('credit_account_balance', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='credit account balance')),
                ('credit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credit_transactions', related_query_name='credit_transaction', to='accounting.Account', verbose_name='credit account')),
                ('debit_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debit_transactions', related_query_name='debit_transaction', to='accounting.Account', verbose_name='debit account')),
            ],
            options={
                'default_permissions': ('view', 'add', 'change', 'delete'),
                'verbose_name_plural': 'transactions',
                'verbose_name': 'transaction',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='account_subtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', related_query_name='account', to='accounting.AccountSubtype', verbose_name='account subtype'),
        ),
        migrations.AddField(
            model_name='account',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', related_query_name='account', to='accounting.Ledger', verbose_name='ledger'),
        ),
        migrations.AlterUniqueTogether(
            name='ledger',
            unique_together=set([('company', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='accountsubtype',
            unique_together=set([('company', 'name')]),
        ),
        migrations.AlterIndexTogether(
            name='accountsubtype',
            index_together=set([('company', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('ledger', 'code')]),
        ),
    ]
