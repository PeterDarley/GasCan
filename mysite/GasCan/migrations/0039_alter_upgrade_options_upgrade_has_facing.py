# Generated by Django 4.1.4 on 2022-12-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0038_rename_slots_weapon_build_slots'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upgrade',
            options={'ordering': ['cost', 'name']},
        ),
        migrations.AddField(
            model_name='upgrade',
            name='has_facing',
            field=models.BooleanField(default=False),
        ),
    ]
