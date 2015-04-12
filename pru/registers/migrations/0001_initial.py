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
                ('contractor', models.CharField(default=b'u', help_text='Name of each contractor', max_length=2, verbose_name='Contractor data', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('id_data', models.CharField(default=b'u', help_text='Machine readable of contractor eg. KRS, NIP, REGON', max_length=2, verbose_name='ID data of contractor', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('value', models.CharField(default=b'u', help_text='Value of each contract are published', max_length=2, verbose_name='Value of contract', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('privacy', models.CharField(default=b'u', help_text='Name of contractor, even individual person', max_length=2, verbose_name='Individual person name', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('text', models.CharField(default=b'u', help_text='Datasheet are published as text', max_length=2, verbose_name='Text format', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('comparable', models.CharField(default=b'u', help_text='Data are published in comparable form eg. spreadsheet, not PDF', max_length=2, verbose_name='Comparable', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('scan', models.CharField(default=b'u', help_text='Scan of most contract without enquire', max_length=2, verbose_name='Scan', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('spending', models.CharField(default=b'u', help_text='Published data contains information about spneding without contracts too', max_length=2, verbose_name='Information about spending', choices=[(b'y', 'yes'), (b'no', 'no'), (b'u', 'unknown')])),
                ('comment', models.TextField(help_text='Extra information about registers eg. story of publishing, heroes', verbose_name='Comment')),
                ('lat', models.CharField(max_length=100, null=True, verbose_name='Longtitude', blank=True)),
                ('lng', models.CharField(max_length=100, null=True, verbose_name='Langtitude', blank=True)),
                ('url', models.URLField(verbose_name='URL of publication')),
                ('public', models.BooleanField(default=False, help_text='Mark to publish on site', verbose_name='Public')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified', models.DateTimeField(help_text='Date of last modification of this object', verbose_name='Last modification date', auto_now=True)),
                ('community', models.ForeignKey(verbose_name='Community', to='teryt.JednostkaAdministracyjna')),
                ('user', models.ForeignKey(verbose_name='Reporter', to=settings.AUTH_USER_MODEL, help_text='User who report contracts to us')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
