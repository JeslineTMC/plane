# Generated by Django 4.2.10 on 2024-03-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='is_telemetry_anonymous',
            field=models.BooleanField(default=False),
        ),
    ]