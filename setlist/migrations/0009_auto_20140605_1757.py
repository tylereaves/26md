# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0008_auto_20140321_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='source',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='show',
            name='leg',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
