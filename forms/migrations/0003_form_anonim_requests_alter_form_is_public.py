# Generated by Django 4.1.4 on 2022-12-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='anonim_requests',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]