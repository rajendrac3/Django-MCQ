# Generated by Django 2.0.1 on 2018-03-17 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]