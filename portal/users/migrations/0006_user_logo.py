# Generated by Django 2.2.1 on 2019-07-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190610_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.TextField(blank=True),
        ),
    ]
