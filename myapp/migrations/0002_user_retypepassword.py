# Generated by Django 5.0.3 on 2024-03-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='RetypePassword',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
