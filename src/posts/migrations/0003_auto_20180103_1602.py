# Generated by Django 2.0.1 on 2018-01-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180103_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]
