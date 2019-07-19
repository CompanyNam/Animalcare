# Generated by Django 2.1.2 on 2019-03-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_event_event_little_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image1',
            field=models.ImageField(blank=True, upload_to='media/animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='donor',
            field=models.ManyToManyField(blank=True, to='home.Donor_Details'),
        ),
    ]