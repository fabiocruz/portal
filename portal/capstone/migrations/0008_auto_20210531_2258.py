# Generated by Django 3.2.3 on 2021-05-31 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("capstone", "0007_auto_20210523_1559"),
    ]

    operations = [
        migrations.RenameField(
            model_name="duedatapoint",
            old_name="student",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="studentapi",
            old_name="student",
            new_name="user",
        ),
    ]
