# Generated by Django 5.1.1 on 2024-12-01 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printing', '0003_rename_papertype_history_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='Quantity',
        ),
    ]
