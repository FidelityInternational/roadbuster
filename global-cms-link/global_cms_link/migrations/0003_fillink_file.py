# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 22:00
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('global_cms_link', '0002_auto_20180801_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillink',
            name='file',
            field=filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='filer.File'),
        ),
    ]