# Generated by Django 5.1.4 on 2025-01-01 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_userprofile_blood_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phohne_number',
            new_name='phone_number',
        ),
    ]
