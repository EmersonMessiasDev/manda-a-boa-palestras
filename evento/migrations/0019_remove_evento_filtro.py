# Generated by Django 4.2 on 2023-04-23 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0018_evento_filtro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='filtro',
        ),
    ]
