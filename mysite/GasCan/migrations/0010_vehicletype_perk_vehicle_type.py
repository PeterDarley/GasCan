# Generated by Django 4.1.4 on 2022-12-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0009_rename_perk_type_perk_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('weight', models.CharField(choices=[('Lightweight', 'Lightweight'), ('Middleweight', 'Middleweight'), ('Heavyweight', 'Heavyweight')], max_length=250)),
                ('hull', models.PositiveSmallIntegerField()),
                ('handling', models.PositiveSmallIntegerField()),
                ('max_gear', models.PositiveSmallIntegerField()),
                ('crew', models.PositiveSmallIntegerField()),
                ('build_slots', models.PositiveSmallIntegerField()),
                ('cost', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='perk',
            name='vehicle_type',
            field=models.ManyToManyField(blank=True, to='GasCan.vehicletype'),
        ),
    ]
