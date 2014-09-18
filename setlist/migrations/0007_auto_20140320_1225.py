# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0006_setlistsong_pos'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.CharField(default='', max_length=255, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='show',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='song',
            name='author',
            field=models.ForeignKey(to_field=u'id', blank=True, to='setlist.Person', null=True),
        ),
    ]
