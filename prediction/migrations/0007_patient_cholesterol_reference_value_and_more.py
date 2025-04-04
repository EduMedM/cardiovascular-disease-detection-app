# Generated by Django 4.2 on 2023-11-10 22:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("prediction", "0006_alter_patient_exercise_induced_angina"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="cholesterol_reference_value",
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name="patient",
            name="date_of_birth",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="patient",
            name="id_num",
            field=models.IntegerField(default=1000000),
        ),
        migrations.AddField(
            model_name="patient",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="patient",
            name="number_of_vessels",
            field=models.IntegerField(
                choices=[(0, "Ninguno"), (1, "Uno"), (2, "Dos"), (3, "Tres")]
            ),
        ),
    ]
