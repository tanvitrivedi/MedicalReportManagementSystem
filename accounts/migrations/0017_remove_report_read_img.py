# Generated by Django 3.0.7 on 2020-07-09 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200709_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='read_img',
        ),
    ]
