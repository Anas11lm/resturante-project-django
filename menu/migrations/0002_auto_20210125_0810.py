# Generated by Django 3.1.5 on 2021-01-25 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='ingrediance',
            new_name='ingredients',
        ),
    ]
