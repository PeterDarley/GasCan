# Generated by Django 4.1.4 on 2022-12-10 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GasCan', '0006_sponsor_alter_perk_perk_class_perk_sponsor'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
