# Generated by Django 3.0.7 on 2020-07-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200707_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='read_img',
            field=models.TextField(blank=True),
        ),
    ]
