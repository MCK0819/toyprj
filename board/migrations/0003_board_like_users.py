# Generated by Django 3.1.6 on 2022-12-21 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('board', '0002_board_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_users',
            field=models.ManyToManyField(related_name='like_boards', to='user.User'),
        ),
    ]