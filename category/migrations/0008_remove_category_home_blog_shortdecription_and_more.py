# Generated by Django 5.2.1 on 2025-06-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_category_home_blog_shortdecription_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='home_blog_shortdecription',
        ),
        migrations.RemoveField(
            model_name='category',
            name='home_blog_title',
        ),
        migrations.AddField(
            model_name='category_page',
            name='home_blog_shortdecription',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category_page',
            name='home_blog_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
