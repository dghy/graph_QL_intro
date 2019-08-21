# Generated by Django 2.2.3 on 2019-08-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='azimuth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='dec',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='elevation',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='observer_altitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='observer_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='observer_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='ra',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='satellite',
            name='norad_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
