# Generated by Django 4.1.4 on 2022-12-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_alter_form_author_alter_formrequest_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
