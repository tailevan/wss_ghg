# Generated by Django 4.2.3 on 2024-02-17 01:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory_Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029)])),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerant_EF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('GWP', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Wastewater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Taxi/ Grab Car', 'Taxi/ Grab Car'), ('Motorbike (Grab)', 'Motorbike (Grab)'), ('Electric Taxi (Xanh Taxi)', 'Electric Taxi (Xanh Taxi)')], max_length=40)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Refrigerant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('R22', 'R22'), ('R410A', 'R410A'), ('HFC-134a', 'HFC-134a'), ('R600a', 'R600a')], max_length=10)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Land line', 'Land line'), ('Tablet', 'Tablet'), ('Phone (Multifunction Device)', 'Phone (Multifunction Device)'), ('Camera Battery', 'Camera Battery'), ('Office Paper', 'Office Paper'), ('Toilet Paper', 'Toilet Paper'), ('Mixed Can', 'Mixed Can'), ('Office Chair', 'Office Chair'), ('Wooden Table', 'Wooden Table'), ('Bean Bag Chair', 'Bean Bag Chair'), ('Monitor - Destop', 'Monitor - Destop'), ('Office Desk', 'Office Desk'), ('Bottled Water (m3)', 'Bottled Water (m3)')], max_length=30)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Freighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(choices=[('Electric Bike', 'Electric Bike'), ('Truck', 'Truck'), ('Train', 'Train'), ('Ship', 'Ship'), ('Airplane', 'Airplane')], max_length=40)),
                ('agent', models.CharField(choices=[('Xanh SM', 'Xanh SM'), ('Grab', 'Grab'), ('Viettel Post', 'Viettel Post'), ('DHL', 'DHL'), ('UPS', 'UPS'), ('FedEx', 'FedEx'), ('Vietnam Post', 'Vietnam Post')], max_length=40)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Domestic (Economy Class)', 'Domestic (Economy Class)'), ('International (Economy Class)', 'International (Economy Class)')], max_length=40)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('passenger', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Electricity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Disposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Carton Paper (Mixed Paper General)', 'Carton Paper (Mixed Paper General)'), ('Garbage (Mixed MSW)', 'Garbage (Mixed MSW)'), ('Plastic (Mixed Plastic)', 'Plastic (Mixed Plastic)')], max_length=40)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Commute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(choices=[('Nguyen Thuy Trang', 'Nguyen Thuy Trang'), ('Frank Pogade', 'Frank Pogade'), ('Than Xuan Mai', 'Than Xuan Mai'), ('Vu Thi Thom', 'Vu Thi Thom'), ('Chan', 'Chan'), ('Markus Klemmer', 'Markus Klemmer'), ('Nguyen Thi Thuy Trang', 'Nguyen Thi Thuy Trang'), ('Le Van Tai', 'Le Van Tai')], max_length=30)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('workdays', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(365)])),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('Vietnam', 'Vietnam'), ('Germany', 'Germany'), ('Hong Kong', 'Hong Kong'), ('Singapore', 'Singapore'), ('Thailand', 'Thailand'), ('Malaysia', 'Malaysia')], max_length=40)),
                ('night', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField()),
                ('inventory_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ghg_inventory.inventory_year')),
            ],
        ),
    ]
