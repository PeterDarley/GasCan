# Generated by Django 4.1.4 on 2022-12-17 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0024_alter_vehicletype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletype',
            name='sponsors_rule',
            field=models.CharField(choices=[('Include', 'Include'), ('Exclude', 'Exclude')], default='Exclude', max_length=250),
        ),
    ]
