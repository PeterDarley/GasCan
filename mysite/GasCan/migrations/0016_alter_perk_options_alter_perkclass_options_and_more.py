# Generated by Django 4.1.4 on 2022-12-14 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0015_vehicletype_trailer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perk',
            options={'ordering': ['cost', 'name']},
        ),
        migrations.AlterModelOptions(
            name='perkclass',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='perk',
            old_name='vehicle_type',
            new_name='vehicle_types',
        ),
    ]
