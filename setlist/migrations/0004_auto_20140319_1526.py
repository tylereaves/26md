# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0003_venue_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue', models.ForeignKey(to='setlist.Venue', to_field=u'id')),
                ('tour', models.ForeignKey(to='setlist.Tour', to_field=u'id')),
                ('date', models.DateField()),
                ('setlist', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SetlistSong',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.ForeignKey(to='setlist.Show', to_field=u'id')),
                ('song', models.ForeignKey(to='setlist.Song', to_field=u'id')),
                ('order', models.IntegerField()),
                ('set', models.CharField(max_length=1, choices=[('1', '1st Set'), ('2', '2nd Set'), ('3', '3rd Set'), ('E', 'Encore')])),
                ('notes', models.TextField(default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='venue',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='author',
            field=models.ForeignKey(to='setlist.Person', to_field=u'id', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='song',
            name='notes',
            field=models.TextField(default='', blank=True),
            preserve_default=True,
        ),
    ]
