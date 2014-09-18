# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0009_auto_20140605_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterTour',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tour',
            name='master_tour',
            field=models.ForeignKey(to='setlist.MasterTour', to_field=u'id', null=True),
            preserve_default=True,
        ),
    ]
