# Generated by Django 4.2.6 on 2024-01-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_remove_teacher_social1_remove_teacher_social2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='instagram',
        ),
        migrations.AddField(
            model_name='teacher',
            name='social1',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка на соцсеть 1'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='social2',
            field=models.CharField(max_length=255, null=True, verbose_name='Ссылка на соцсеть 2'),
        ),
    ]
