# Generated by Django 2.0.5 on 2018-05-10 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startvote', '0008_auto_20180509_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startvote.User')),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='creat_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_target',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='option_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='option_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_state',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='vote_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startvote.Vote'),
        ),
    ]
