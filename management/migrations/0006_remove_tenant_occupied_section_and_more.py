# Generated by Django 5.1 on 2024-08-30 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_rentalpayments_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='occupied_section',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='property',
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=20)),
                ('floor', models.CharField(blank=True, max_length=20, null=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='management.property')),
            ],
        ),
        migrations.AddField(
            model_name='tenant',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='management.unit'),
        ),
    ]
