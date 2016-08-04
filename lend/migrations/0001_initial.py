# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 01:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('price_h', models.CharField(help_text='숫자로만 입력', max_length=10, validators=[lend.models.price_validator])),
                ('price_d', models.CharField(help_text='숫자로만 입력', max_length=10, validators=[lend.models.price_validator])),
                ('calendar', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('m_type', models.CharField(max_length=30)),
                ('detail', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='lender',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lend.Machine'),
        ),
        migrations.AddField(
            model_name='lender',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]