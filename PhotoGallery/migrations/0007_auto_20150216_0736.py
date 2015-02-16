# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0006_auto_20150214_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 16, 7, 36, 29, 646804, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
