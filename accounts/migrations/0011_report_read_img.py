# Generated by Django 3.0.7 on 2020-07-05 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_read_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='read_img',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
