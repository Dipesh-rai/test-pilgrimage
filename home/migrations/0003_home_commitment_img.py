# Generated by Django 5.2.1 on 2025-06-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_home_commitment_description_home_commitment_heading_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='commitment_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='sacredsite'),
        ),
    ]
