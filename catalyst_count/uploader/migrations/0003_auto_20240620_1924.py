# Generated by Django 3.2.25 on 2024-06-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_querybody'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querybody',
            old_name='city',
            new_name='locality',
        ),
        migrations.RemoveField(
            model_name='querybody',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='querybody',
            name='state',
        ),
    ]
