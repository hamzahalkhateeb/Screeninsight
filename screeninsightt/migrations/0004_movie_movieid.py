# Generated by Django 4.2.7 on 2024-02-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screeninsightt', '0003_rename_likedmovies_likedmovies_likedmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movieid',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
