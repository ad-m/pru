# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teryt', '0005_auto_20150225_1244'),
        ('registers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('teryt.jednostkaadministracyjna',),
        ),
        migrations.AlterField(
            model_name='register',
            name='community',
            field=models.ForeignKey(verbose_name='Community', to='registers.Community'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='comparable',
            field=models.IntegerField(default=2, help_text='Data are published in comparable form eg. spreadsheet, not PDF', verbose_name='Comparable', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='contractor',
            field=models.IntegerField(default=2, help_text='Name of each contractor', verbose_name='Contractor data', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='id_data',
            field=models.IntegerField(default=2, help_text='Machine readable of contractor eg. KRS, REGON', verbose_name='ID data of contractor', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='privacy',
            field=models.IntegerField(default=2, help_text='Name of contractor, even individual person', verbose_name='Individual person name', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='scan',
            field=models.IntegerField(default=2, help_text='Scan of most contract without enquire', verbose_name='Scan', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='spending',
            field=models.IntegerField(default=2, help_text='Published data contains information about spneding without contracts too', verbose_name='Information about spending', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='text',
            field=models.IntegerField(default=2, help_text='Datasheet are published as text', verbose_name='Text format', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='register',
            name='value',
            field=models.IntegerField(default=2, help_text='Value of each contract are published', verbose_name='Value of contract', choices=[(0, 'yes'), (1, 'no'), (2, 'unknown')]),
            preserve_default=True,
        ),
    ]
