# Generated by Django 5.2.1 on 2025-06-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sacredsite', '0015_tourbooking_notes_tourbooking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(default=None, max_length=250, null=True, upload_to='sacredsite')),
                ('img_src', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
