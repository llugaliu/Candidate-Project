# Generated by Django 4.2.5 on 2023-09-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_candiate_email_email_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_email', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('chat', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]