# Generated by Django 4.2.11 on 2024-11-29 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_messages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
