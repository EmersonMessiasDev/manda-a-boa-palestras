# Generated by Django 4.2 on 2023-04-21 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0002_pergunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='qrCode',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
