# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0004_auto_20140319_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='setlistsong',
            name='segue',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
