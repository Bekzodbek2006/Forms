# Generated by Django 4.1.4 on 2022-12-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0021_form_submit_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='formrequest',
            name='as_anonim',
            field=models.BooleanField(default=False),
        ),
    ]