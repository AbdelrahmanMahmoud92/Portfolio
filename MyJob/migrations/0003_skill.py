# Generated by Django 4.2.8 on 2024-01-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyJob', '0002_link_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=250)),
            ],
        ),
    ]
