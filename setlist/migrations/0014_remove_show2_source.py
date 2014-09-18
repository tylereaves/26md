# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0013_show2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show2',
            name='source',
        ),
    ]
