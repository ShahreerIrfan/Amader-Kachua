# Generated by Django 5.1.4 on 2025-01-01 12:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phohne_number', models.CharField(max_length=20, null=True)),
                ('village', models.CharField(max_length=80, null=True)),
                ('photo', models.ImageField(null=True, upload_to='user/profile_photo')),
                ('union', models.CharField(blank=True, choices=[('1 No Union', '1 No Union'), ('2 No Union', '2 No Union'), ('3 No Union', '3 No Union'), ('4 No Union', '4 No Union'), ('5 No Union', '5 No Union'), ('6 No Union', '6 No Union'), ('7 No Union', '7 No Union'), ('8 No Union', '8 No Union'), ('9 No Union', '9 No Union'), ('10 No Union', '10 No Union')], max_length=20, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('address', models.TextField(null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True)),
                ('occupation', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
