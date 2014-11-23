# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_one', models.CharField(max_length=100)),
                ('address_two', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('stripe_id', models.CharField(max_length=30, blank=True)),
                ('user_rec', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'subscribers',
            },
            bases=(models.Model,),
        ),
    ]
