# Generated by Django 4.0.4 on 2022-04-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0006_alter_userbook_easiness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='interval',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
