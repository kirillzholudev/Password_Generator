# Generated by Django 4.2.4 on 2023-09-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_savedpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedpassword',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
