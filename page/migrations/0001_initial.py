# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_instruccion', models.IntegerField(null=True, blank=True)),
                ('nro_expediente', models.IntegerField(null=True, blank=True)),
                ('anio', models.IntegerField(null=True, blank=True)),
                ('juzgado', models.CharField(max_length=45, null=True, blank=True)),
                ('agraviado', models.CharField(max_length=100, null=True, blank=True)),
                ('inculpado', models.CharField(max_length=100, null=True, blank=True)),
                ('materia', models.CharField(max_length=150, null=True, blank=True)),
                ('nro_fojas', models.IntegerField(null=True, verbose_name=b'Foja(s)', blank=True)),
                ('nro_legajo', models.IntegerField(null=True, verbose_name=b'Legajo', blank=True)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model,),
        ),
    ]
