# Generated by Django 4.2 on 2023-04-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0011_alter_evento_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
