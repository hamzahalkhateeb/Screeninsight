# Generated by Django 4.2.7 on 2024-02-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screeninsightt', '0008_commenttv_tv_watchlisttv_replytv_likedtv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tv',
            name='comments',
            field=models.ManyToManyField(to='screeninsightt.commenttv'),
        ),
    ]
