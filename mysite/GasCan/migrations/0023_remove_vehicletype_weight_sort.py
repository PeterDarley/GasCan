# Generated by Django 4.1.4 on 2022-12-17 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0022_vehicletype_weight_sort_alter_vehicletype_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicletype',
            name='weight_sort',
        ),
    ]
