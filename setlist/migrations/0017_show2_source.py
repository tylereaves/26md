# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0016_show2_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='source',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
