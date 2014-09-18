# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0014_remove_show2_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show2',
            name='tour',
        ),
        migrations.RemoveField(
            model_name='show2',
            name='venue',
        ),
    ]
