# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0012_remove_show_leg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue', models.ForeignKey(to='setlist.Venue', to_field='id')),
                ('tour', models.ForeignKey(to='setlist.Tour', to_field='id')),
                ('date', models.DateField(db_index=True)),
                ('setlist', models.TextField(default=b'', blank=True)),
                ('notes', models.TextField(default=b'', blank=True)),
                ('source', models.TextField(default=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
