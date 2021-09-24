# Generated by Django 3.2.4 on 2021-09-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_user_applying_for_scholarship'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='can_attend_next',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='can_graduate',
            field=models.BooleanField(default=True),
        ),
    ]
