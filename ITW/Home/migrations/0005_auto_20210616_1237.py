# Generated by Django 3.2.3 on 2021-06-16 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20210616_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='bday',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='city',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='state',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='adress',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='adress2',
        ),
    ]
