# Generated by Django 2.0.5 on 2018-05-07 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startvote', '0002_artivle_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artivle',
            name='pub_time',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
