# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shortuuidfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('account', models.ForeignKey(to='accounts.Account')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
            bases=(models.Model,),
        ),
    ]
