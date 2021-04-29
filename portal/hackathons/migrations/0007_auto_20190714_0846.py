# Generated by Django 2.2.1 on 2019-07-14 08:46

from django.db import migrations, models
import django.db.models.deletion
import portal.hackathons.models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("hackathons", "0006_auto_20190703_1857"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hackathon",
            name="scoring_fcn",
        ),
        migrations.RemoveField(
            model_name="hackathon",
            name="y_true",
        ),
        migrations.RemoveField(
            model_name="team",
            name="score",
        ),
        migrations.RemoveField(
            model_name="team",
            name="submissions",
        ),
        migrations.RemoveField(
            model_name="team",
            name="token",
        ),
        migrations.AddField(
            model_name="hackathon",
            name="data_file",
            field=models.FileField(
                null=True, upload_to=portal.hackathons.models.random_path
            ),
        ),
        migrations.AddField(
            model_name="hackathon",
            name="script_file",
            field=models.FileField(
                null=True, upload_to=portal.hackathons.models.random_path
            ),
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("score", models.FloatField(default=0.0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        ),
    ]
