# Generated by Django 4.2.8 on 2024-01-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyJob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='cv',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
