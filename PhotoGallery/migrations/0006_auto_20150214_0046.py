# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0005_auto_20150214_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 13, 23, 46, 15, 254062, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='imgThumb',
            field=models.ImageField(upload_to='', default=None),
            preserve_default=True,
        ),
    ]
