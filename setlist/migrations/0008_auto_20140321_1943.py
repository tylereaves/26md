# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0007_auto_20140320_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tour',
            name='start_date',
            field=models.DateField(default='2050-01-01', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='show',
            name='setlist',
            field=models.TextField(default='', blank=True),
        ),
    ]
