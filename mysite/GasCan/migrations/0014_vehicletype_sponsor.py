# Generated by Django 4.1.4 on 2022-12-13 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0013_weapon_ammo_weapon_attack_dice_weapon_slots_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GasCan.sponsor'),
        ),
    ]
