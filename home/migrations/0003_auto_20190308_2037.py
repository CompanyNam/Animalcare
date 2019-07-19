# Generated by Django 2.1.2 on 2019-03-08 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_menulanguages_language_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=122)),
            ],
        ),
        migrations.RemoveField(
            model_name='menulanguages',
            name='language',
        ),
        migrations.DeleteModel(
            name='MenuLanguages',
        ),
        migrations.AddField(
            model_name='menu',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Languages'),
            preserve_default=False,
        ),
    ]