# Generated by Django 4.0.4 on 2022-11-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_favorite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
