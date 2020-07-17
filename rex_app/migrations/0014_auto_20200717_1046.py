# Generated by Django 3.0.5 on 2020-07-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rex_app', '0013_question_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='rex_app.Tag'),
        ),
    ]