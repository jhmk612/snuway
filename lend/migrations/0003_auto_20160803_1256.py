# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 03:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lend', '0002_auto_20160801_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lender',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
