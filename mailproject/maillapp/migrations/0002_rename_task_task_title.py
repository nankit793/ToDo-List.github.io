# Generated by Django 3.2.8 on 2021-12-06 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maillapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='title',
        ),
    ]
