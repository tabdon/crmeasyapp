# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField(blank=True)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('phone', models.CharField(max_length=20)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'accounts',
            },
            bases=(models.Model,),
        ),
    ]
