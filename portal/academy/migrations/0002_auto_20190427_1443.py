# Generated by Django 2.0.13 on 2019-04-27 14:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='status',
            field=models.CharField(choices=[('never-submitted', 'Never Submitted'), ('grading', 'Grading...'), ('failed', 'Failed'), ('out-of-date', 'Out-of-date'), ('graded', 'Graded')], default='never-submitted', max_length=1024),
        ),
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('student', 'unit')},
        ),
    ]
