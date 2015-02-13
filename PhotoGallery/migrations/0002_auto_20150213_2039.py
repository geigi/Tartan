# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='discription',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=200, blank=True, null=True),
            preserve_default=True,
        ),
    ]
