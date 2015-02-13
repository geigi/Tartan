# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0003_auto_20150213_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 14, 0, 25, 4, 323449)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='imgPreview',
            field=models.ImageField(upload_to='', default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='imgThumb',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
