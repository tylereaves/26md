# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0005_setlistsong_segue'),
    ]

    operations = [
        migrations.AddField(
            model_name='setlistsong',
            name='pos',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
