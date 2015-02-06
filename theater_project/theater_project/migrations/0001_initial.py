# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('thumbnail', models.CharField(max_length=400)),
                ('rating', models.CharField(max_length=400)),
                ('duration', models.CharField(max_length=400)),

            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('item', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=40)),
                ('thumbnail', models.CharField(max_length=400)),
                ('source', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('descr', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
