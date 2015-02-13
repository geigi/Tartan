# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0004_auto_20150214_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 2, 13, 23, 29, 22, 349154, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
