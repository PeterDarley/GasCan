# Generated by Django 4.1.4 on 2022-12-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0019_remove_vehicletype_sponsor_vehicletype_sponsors'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='sponsors_rule',
            field=models.CharField(blank=True, choices=[('Include', 'Include'), ('Exclude', 'Exclude')], max_length=250, null=True),
        ),
    ]
