# Generated by Django 2.0.1 on 2018-03-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_remove_quiz_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]