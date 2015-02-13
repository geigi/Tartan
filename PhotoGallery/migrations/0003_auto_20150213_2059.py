# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoGallery', '0002_auto_20150213_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='discription',
            new_name='description',
        ),
    ]
