# Generated by Django 2.1.2 on 2019-03-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20190326_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='upcoming_events_slogan',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='upcoming_events_title',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]