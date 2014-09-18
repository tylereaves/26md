# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
