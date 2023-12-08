# Generated by Django 4.2.6 on 2023-12-01 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['order'], 'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='display',
            field=models.BooleanField(blank=True, null=True, verbose_name='Отображение'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Порядок вывода'),
        ),
    ]