# Generated by Django 2.0.6 on 2024-03-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=100, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=100, unique=True, verbose_name='Correo')),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['nombre'],
            },
        ),
    ]
