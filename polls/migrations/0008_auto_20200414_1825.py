# Generated by Django 2.1.7 on 2020-04-14 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20200414_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capability',
            old_name='milestone',
            new_name='milestone_name',
        ),
        migrations.RenameField(
            model_name='milestone',
            old_name='project',
            new_name='project_name',
        ),
    ]
