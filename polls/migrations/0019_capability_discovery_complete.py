# Generated by Django 2.1.7 on 2020-04-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20200427_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='capability',
            name='discovery_complete',
            field=models.BooleanField(default=False),
        ),
    ]
