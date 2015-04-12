# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teryt', '0005_auto_20150225_1244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('img', models.ImageField(upload_to=b'', null=True, verbose_name='Featured image', blank=True)),
                ('title', models.CharField(max_length=150, verbose_name='Institution name')),
                ('contractor', models.IntegerField(default=2, help_text='Name of each contractor', verbose_name='Contractor data', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('id_data', models.IntegerField(default=2, help_text='Machine readable of contractor eg. KRS, REGON', verbose_name='ID data of contractor', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('value', models.IntegerField(default=2, help_text='Value of each contract are published', verbose_name='Value of contract', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('privacy', models.IntegerField(default=2, help_text='Name of contractor, even individual person', verbose_name='Individual person name', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('text', models.IntegerField(default=2, help_text='Datasheet are published as text', verbose_name='Text format', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('comparable', models.IntegerField(default=2, help_text='Data are published in comparable form eg. spreadsheet, not PDF', verbose_name='Comparable', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('scan', models.IntegerField(default=2, help_text='Scan of most contract without enquire', verbose_name='Scan', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('spending', models.IntegerField(default=2, help_text='Published data contains information about spneding without contracts too', verbose_name='Information about spending', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')])),
                ('comment', models.TextField(help_text='Extra information about registers eg. story of publishing, heroes', verbose_name='Comment', blank=True)),
                ('lat', models.CharField(max_length=100, null=True, verbose_name='Longtitude', blank=True)),
                ('lng', models.CharField(max_length=100, null=True, verbose_name='Langtitude', blank=True)),
                ('url', models.URLField(verbose_name='URL of publication')),
                ('public', models.BooleanField(default=False, help_text='Mark to publish on site', verbose_name='Public')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified', models.DateTimeField(help_text='Date of last modification of this object', verbose_name='Last modification date', auto_now=True)),
                ('user', models.ForeignKey(verbose_name='Reporter', to=settings.AUTH_USER_MODEL, help_text='User who report contracts to us')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('teryt.jednostkaadministracyjna',),
        ),
        migrations.AddField(
            model_name='register',
            name='community',
            field=models.ForeignKey(verbose_name='Community', to='registers.Community'),
            preserve_default=True,
        ),
    ]
