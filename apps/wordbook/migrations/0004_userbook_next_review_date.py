# Generated by Django 4.0.4 on 2022-04-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0003_alter_userbook_interval_alter_userbook_last_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbook',
            name='next_review_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
