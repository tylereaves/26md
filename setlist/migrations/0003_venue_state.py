# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0002_venue'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='state',
            field=models.CharField(default='', max_length=255),
            preserve_default=True,
        ),
    ]
