# Generated by Django 3.1.7 on 2021-03-04 19:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 3, 4, 19, 9, 44, 166036, tzinfo=utc)),
            preserve_default=False,
        ),
    ]