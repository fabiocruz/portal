# Generated by Django 3.2.3 on 2021-05-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0007_auto_20200517_1511"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grade",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
