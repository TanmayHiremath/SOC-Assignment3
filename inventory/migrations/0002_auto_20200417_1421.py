# Generated by Django 3.0.5 on 2020-04-17 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventory',
            new_name='Machine',
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='Machine',
            new_name='Name',
        ),
    ]