# Generated by Django 2.1.2 on 2019-03-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20190326_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image1',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image10',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image11',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image12',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image13',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image2',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image3',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image4',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image5',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image6',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image7',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image8',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_image9',
            field=models.ImageField(blank=True, upload_to='animal_need_help'),
        ),
        migrations.AlterField(
            model_name='animal_need_help',
            name='animal_is_donated',
            field=models.IntegerField(),
        ),
    ]
