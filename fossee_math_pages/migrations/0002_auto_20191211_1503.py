# Generated by Django 2.2.7 on 2019-12-11 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossee_math_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adduser',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='adduser',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 15, 3, 33, 964988)),
        ),
    ]
