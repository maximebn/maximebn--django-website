# Generated by Django 2.2.6 on 2019-10-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='mapFrameLink',
            field=models.TextField(default=1, verbose_name='adresse de la carte OpenStreetMaps pour intégration dans une iFrame'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='mapLink',
            field=models.TextField(null=True, verbose_name='lien vers la carte OpenStreetMaps.org'),
        ),
    ]
