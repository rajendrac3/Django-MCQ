# Generated by Django 2.0.6 on 2018-07-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_homecategories_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecategories',
            name='reference_id',
            field=models.CharField(max_length=5),
        ),
    ]