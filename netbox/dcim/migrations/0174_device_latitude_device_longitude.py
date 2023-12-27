# Generated by Django 4.1.9 on 2023-05-31 22:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('dcim', '0173_remove_napalm_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]