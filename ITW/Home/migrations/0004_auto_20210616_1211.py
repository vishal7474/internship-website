# Generated by Django 3.2.3 on 2021-06-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_contactus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='zip',
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
