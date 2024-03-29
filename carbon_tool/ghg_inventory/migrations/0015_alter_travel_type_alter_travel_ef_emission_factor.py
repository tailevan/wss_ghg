# Generated by Django 4.2.3 on 2024-02-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghg_inventory', '0014_travel_ef_travel_emission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='type',
            field=models.CharField(choices=[('Taxi - Grab Car', 'Taxi - Grab Car'), ('Motorbike (Grab)', 'Motorbike (Grab)'), ('Electric Taxi (Xanh Taxi)', 'Electric Taxi (Xanh Taxi)')], max_length=40),
        ),
        migrations.AlterField(
            model_name='travel_ef',
            name='emission_factor',
            field=models.DecimalField(decimal_places=10, max_digits=10),
        ),
    ]
