# Generated by Django 5.1.1 on 2024-12-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printer',
            old_name='ConnectionKey',
            new_name='Brand',
        ),
        migrations.RenameField(
            model_name='printer',
            old_name='Building',
            new_name='Model',
        ),
        migrations.AlterField(
            model_name='printer',
            name='Status',
            field=models.CharField(choices=[('Available', 'Available'), ('Maintenance', 'Maintenance')], default='Available', max_length=50),
        ),
    ]
