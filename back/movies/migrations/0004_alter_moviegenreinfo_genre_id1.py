# Generated by Django 4.2.8 on 2024-05-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviegenreinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviegenreinfo',
            name='genre_id1',
            field=models.IntegerField(null=True),
        ),
    ]