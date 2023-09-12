# Generated by Django 4.2.5 on 2023-09-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='email',
            name='date',
        ),
        migrations.RemoveField(
            model_name='email',
            name='user',
        ),
        migrations.AddField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]