# Generated by Django 3.0.5 on 2020-08-07 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rex_app', '0007_question_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='directmessage',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=99),
        ),
    ]
