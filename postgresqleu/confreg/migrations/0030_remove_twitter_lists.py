# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-09 14:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confreg', '0029_drop_mailman_sync'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='twitter_attendeelist',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='twitter_speakerlist',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='twitter_sponsorlist',
        ),
    ]
