# Generated by Django 3.2.4 on 2021-10-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0009_auto_20210531_2258"),
    ]

    operations = [
        migrations.AddField(
            model_name="grade",
            name="on_time",
            field=models.BooleanField(default=True),
        ),
    ]
