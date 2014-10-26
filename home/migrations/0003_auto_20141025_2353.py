# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_originalcomment_replycomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('op_id', models.IntegerField(default=0)),
                ('comment_text', models.CharField(max_length=10000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='replycomment',
            name='op',
        ),
        migrations.DeleteModel(
            name='OriginalComment',
        ),
        migrations.DeleteModel(
            name='ReplyComment',
        ),
    ]
