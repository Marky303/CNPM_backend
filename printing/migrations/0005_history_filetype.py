# Generated by Django 5.1.1 on 2024-12-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing', '0004_remove_history_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='FileType',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]