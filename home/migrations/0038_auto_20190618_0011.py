# Generated by Django 2.1.2 on 2019-06-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20190618_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='report',
        ),
        migrations.AddField(
            model_name='event',
            name='report',
            field=models.ManyToManyField(blank=True, to='home.Report'),
        ),
    ]
