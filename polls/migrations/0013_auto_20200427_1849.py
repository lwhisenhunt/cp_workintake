# Generated by Django 2.1.7 on 2020-04-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200427_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ace_approved',
            field=models.BooleanField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ace_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]