# Generated by Django 4.2.5 on 2023-09-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='company',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='file',
            field=models.FileField(null=True, upload_to='cv'),
        ),
    ]
