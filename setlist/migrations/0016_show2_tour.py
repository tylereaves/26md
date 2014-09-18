# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0015_auto_20140606_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='tour',
            field=models.ForeignKey(to='setlist.Tour', default=1, to_field='id'),
            preserve_default=False,
        ),
    ]
