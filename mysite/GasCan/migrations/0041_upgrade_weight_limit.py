# Generated by Django 4.1.4 on 2022-12-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0040_upgrade_ammo'),
    ]

    operations = [
        migrations.AddField(
            model_name='upgrade',
            name='weight_limit',
            field=models.CharField(blank=True, choices=[(1, 'Lightweight'), (2, 'Middleweight'), (3, 'Heavyweight')], max_length=250, null=True),
        ),
    ]
