# Generated by Django 4.1.7 on 2023-03-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typingsite', '0003_game_gametype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gametype',
            field=models.IntegerField(default=10),
        ),
    ]