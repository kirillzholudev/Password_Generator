# Generated by Django 4.2.4 on 2023-09-08 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_savedpassword_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwordsettings',
            old_name='use_numbers',
            new_name='numbers',
        ),
        migrations.RenameField(
            model_name='passwordsettings',
            old_name='use_special_characters',
            new_name='symbols',
        ),
        migrations.RenameField(
            model_name='passwordsettings',
            old_name='use_uppercase',
            new_name='uppercase',
        ),
    ]
