# Generated by Django 4.2.5 on 2024-06-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0019_user_failed_or_dropped"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="academy_type_preference",
            field=models.CharField(
                blank=True,
                choices=[
                    ("in_person_then_remote", "In-person then remote"),
                    ("remote_then_in_person", "Remote then in-person"),
                    ("remote_only", "Remote only"),
                    ("in_person_only", "In-person only"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
