# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='id',
            new_name='comment_id',
        ),
    ]
