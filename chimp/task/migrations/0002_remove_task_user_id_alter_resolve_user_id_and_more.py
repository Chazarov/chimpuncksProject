# Generated by Django 5.0.6 on 2024-05-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='resolve',
            name='user_id',
            field=models.CharField(max_length=30, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='test',
            name='user_id',
            field=models.CharField(max_length=30, verbose_name='ID пользователя'),
        ),
    ]
