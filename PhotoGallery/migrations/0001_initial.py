# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, max_length=200)),
                ('imgOrig', models.ImageField(upload_to='')),
                ('imgPreview', models.ImageField(null=True, default=None, blank=True, upload_to='')),
                ('imgThumb', models.ImageField(null=True, default=None, blank=True, upload_to='')),
                ('album', models.ForeignKey(to='PhotoGallery.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
