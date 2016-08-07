# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lend', '0003_auto_20160803_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='lender',
            name='tags',
            field=models.ManyToManyField(to='lend.Tag'),
        ),
    ]
