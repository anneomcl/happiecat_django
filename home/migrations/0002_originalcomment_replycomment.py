# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('comment_text', models.CharField(max_length=10000)),
                ('post_time', models.DateTimeField(verbose_name='date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('comment_text', models.CharField(max_length=10000)),
                ('post_time', models.DateTimeField(verbose_name='date published')),
                ('op', models.ForeignKey(to='home.OriginalComment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
