# Generated by Django 4.2.11 on 2024-05-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster_path',
            field=models.TextField(null=True),
        ),
    ]