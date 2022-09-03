# Generated by Django 4.1 on 2022-09-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_clase1_clase2_clase3_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('area_control', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economia', models.CharField(max_length=50)),
                ('juegos', models.CharField(max_length=50)),
                ('naturaleza', models.CharField(max_length=50)),
                ('internet', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('registro', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='clase1',
        ),
        migrations.DeleteModel(
            name='clase2',
        ),
        migrations.DeleteModel(
            name='clase3',
        ),
    ]
