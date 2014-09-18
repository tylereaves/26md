# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0010_auto_20140606_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='state',
            field=models.CharField(default='', max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='city',
            field=models.TextField(db_index=True),
        ),
    ]
