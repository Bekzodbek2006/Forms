# Generated by Django 4.1.4 on 2022-12-20 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0014_alter_formrequest_form_submitsuccessmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitsuccessmessage',
            name='form',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='submit_success_form', to='forms.form'),
        ),
    ]