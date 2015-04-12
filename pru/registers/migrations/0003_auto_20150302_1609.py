# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0002_auto_20150302_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='comment',
            field=models.TextField(help_text='Extra information about registers eg. story of publishing, heroes', verbose_name='Comment', blank=True),
            preserve_default=True,
        ),
    ]
