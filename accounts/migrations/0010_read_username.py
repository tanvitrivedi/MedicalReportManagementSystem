# Generated by Django 3.0.7 on 2020-07-05 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200704_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='read',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
