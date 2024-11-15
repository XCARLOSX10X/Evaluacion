# Generated by Django 5.1.3 on 2024-11-14 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('cedula', models.CharField(max_length=10, null=True, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, max_length=50, null=True)),
                ('anio', models.PositiveIntegerField()),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('placa', models.CharField(max_length=10, null=True, unique=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='Reparacion.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_ingreso', models.DateField()),
                ('fecha_salida', models.DateField(blank=True, null=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Completado', 'Completado')], max_length=20)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('En curso', 'En curso'), ('Finalizado', 'Finalizado')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.cliente')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.vehiculo')),
            ],
        ),
    ]
