# Generated by Django 4.2.6 on 2024-01-17 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='package',
            options={'ordering': ['id'], 'verbose_name': 'Пакет', 'verbose_name_plural': 'Пакеты'},
        ),
    ]
