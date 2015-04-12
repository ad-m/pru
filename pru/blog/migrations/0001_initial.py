# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('img', models.ImageField(upload_to=b'', null=True, verbose_name='Featured image', blank=True)),
                ('title', models.CharField(max_length=150, verbose_name='Post title')),
                ('public', models.BooleanField(default=False, help_text='Mark to publish on site', verbose_name='Public')),
                ('comment', models.TextField(verbose_name='Comment', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified', models.DateTimeField(help_text='Date of last modification of this object', verbose_name='Last modification date', auto_now=True)),
                ('registers', models.ManyToManyField(to='registers.Register', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('title', models.CharField(max_length=150, verbose_name='Tag name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
