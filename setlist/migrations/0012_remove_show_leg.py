# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0011_auto_20140606_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name=b'leg',
        ),
    ]
