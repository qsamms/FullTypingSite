# Generated by Django 4.1.7 on 2023-03-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typingsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='game',
            name='speed',
            field=models.IntegerField(),
        ),
    ]
