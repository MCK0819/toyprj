# Generated by Django 3.1.6 on 2022-12-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('board', '0003_board_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='like_users',
        ),
        migrations.CreateModel(
            name='LikeUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_users', models.ManyToManyField(related_name='like_boards', to='user.User')),
            ],
        ),
    ]
