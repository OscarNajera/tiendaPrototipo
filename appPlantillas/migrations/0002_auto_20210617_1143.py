# Generated by Django 3.1.7 on 2021-06-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPlantillas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contrasena',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=50),
        ),
    ]