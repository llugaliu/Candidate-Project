# Generated by Django 4.2.5 on 2023-09-11 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_email_chat_remove_email_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='candiate_email',
            new_name='name',
        ),
    ]