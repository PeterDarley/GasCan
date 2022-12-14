# Generated by Django 4.1.4 on 2022-12-17 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0021_alter_perk_sponsor_alter_perk_vehicle_types_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='weight_sort',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='weight',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Lightweight'), (2, 'Middleweight'), (3, 'Heavyweight')]),
        ),
    ]
