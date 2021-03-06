# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 01:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='document',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sales.Document'),
            preserve_default=False,
        ),
    ]
