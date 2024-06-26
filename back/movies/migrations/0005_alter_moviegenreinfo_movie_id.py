# Generated by Django 4.2.8 on 2024-05-20 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_moviegenreinfo_genre_id1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviegenreinfo',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_genre_id', to='movies.movie'),
        ),
    ]
