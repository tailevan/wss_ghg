# Generated by Django 4.2.3 on 2024-02-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghg_inventory', '0015_alter_travel_type_alter_travel_ef_emission_factor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight_EF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40)),
                ('emission_factor', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='emission',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
