# Generated by Django 2.1.2 on 2019-01-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_auto_20190123_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]