# Generated by Django 2.1.7 on 2020-04-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20200428_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='capability',
            name='benefit',
            field=models.CharField(max_length=200, null=True),
        ),
    ]