# Generated by Django 2.1.7 on 2020-04-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_capability_target_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capability',
            old_name='name',
            new_name='capability',
        ),
        migrations.AlterField(
            model_name='capability',
            name='product_type',
            field=models.CharField(choices=[('Zeus', 'Zeus'), ('Athena', 'Athena'), ('Monitor', 'Monitor')], default='service', max_length=200, null=True),
        ),
    ]
