# Generated by Django 4.0.4 on 2022-04-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0005_alter_userbook_easiness_alter_userbook_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='easiness',
            field=models.FloatField(default=0),
        ),
    ]
