# Generated by Django 2.2.3 on 2020-05-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hackathons", "0009_submission_hackathon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendance",
            name="will_attend",
        ),
        migrations.AlterField(
            model_name="attendance",
            name="present",
            field=models.BooleanField(default=True),
        ),
    ]
