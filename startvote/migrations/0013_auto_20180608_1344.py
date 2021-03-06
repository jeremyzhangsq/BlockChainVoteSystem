# Generated by Django 2.0.5 on 2018-06-08 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startvote', '0012_auto_20180510_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='local_Key_pool',
            fields=[
                ('key_id', models.IntegerField(primary_key=True, serialize=False)),
                ('public_key', models.CharField(max_length=300)),
                ('private_key', models.CharField(max_length=300)),
                ('statue', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='vote_selection',
            name='selection_id',
        ),
        migrations.RemoveField(
            model_name='vote_selection',
            name='vote_id',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='option_content',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='option_size',
        ),
        migrations.AddField(
            model_name='entry',
            name='identity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='selection',
            name='vote_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='startvote.Vote'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='selection',
            name='img',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Vote_selection',
        ),
    ]
