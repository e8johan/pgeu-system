# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-09 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0012_generic_bank_transfers'),
        ('trustlypayment', '0003_payment_refactor'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrustlyWithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gluepayid', models.BigIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('message', models.CharField(blank=True, max_length=200)),
                ('paymentmethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.InvoicePaymentMethod')),
            ],
        ),
    ]
