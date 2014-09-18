# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0018_show2_venue'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Show2',
        ),
    ]
