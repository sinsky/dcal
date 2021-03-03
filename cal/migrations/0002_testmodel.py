# Generated by Django 3.1.7 on 2021-03-03 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('startDay', models.DateTimeField(default=datetime.datetime(2021, 3, 3, 5, 28, 12, 382258, tzinfo=utc), verbose_name='開始')),
            ],
        ),
    ]