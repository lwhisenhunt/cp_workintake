# Generated by Django 2.1.7 on 2020-04-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20200427_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ace_approved',
            field=models.BooleanField(default=False),
        ),
    ]