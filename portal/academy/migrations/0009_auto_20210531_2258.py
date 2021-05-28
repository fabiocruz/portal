# Generated by Django 3.2.3 on 2021-05-31 22:58

from django.db import migrations, models
import portal.academy.models


class Migration(migrations.Migration):

    dependencies = [
        ("academy", "0008_alter_grade_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="grade",
            old_name="student",
            new_name="user",
        ),
        migrations.AddField(
            model_name="grade",
            name="feedback",
            field=models.FileField(
                null=True, upload_to=portal.academy.models.feedback_path
            ),
        ),
        migrations.AlterField(
            model_name="grade",
            name="status",
            field=models.CharField(
                choices=[
                    ("never-submitted", "Unsubmitted"),
                    ("sent", "Sent"),
                    ("grading", "Grading"),
                    ("failed", "Grading failed"),
                    ("out-of-date", "Out-of-date"),
                    ("checksum-failed", "Checksum verification failed"),
                    ("graded", "Graded"),
                ],
                default="never-submitted",
                max_length=1024,
            ),
        ),
    ]
