# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0017_show2_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='show2',
            name='venue',
            field=models.ForeignKey(to='setlist.Venue', default=1, to_field='id'),
            preserve_default=False,
        ),
    ]
