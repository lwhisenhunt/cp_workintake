# Generated by Django 2.1.7 on 2020-04-14 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200414_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capability',
            name='name',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='name',
        ),
        migrations.AddField(
            model_name='capability',
            name='capability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Project'),
        ),
    ]