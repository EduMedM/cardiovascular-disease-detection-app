from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

sex_choices = ((0, 'Femenino'),(1, 'Masculino'))
cp_choice = ((0,'Ninguno'),(1, 'Angina Típica'),(2, 'Angina Atípica'),(3, 'Dolor No Anginoso'),(4, 'Asintómatico'))
fasting_blood_sugar_choices = ((1,'> 120 mg/dl'),((0,'< 120 mg/dl')))
resting_ecg_choices = ((0, 'Normal'),(1, 'Anomalía de la Onda ST-T '),(2, 'Hipertrofia Ventricular Izquierda'))
exercise_induced_angina_choices = ((0, 'No'),(1, 'Sí'))
st_slope_choices = ((1, 'Pendiente Ascendente'),(2, 'Plano'),(3, 'Pendiente Descendente'))
number_of_vessels_choices = ((0, 'Ninguno'),(1, 'Uno'),(2, 'Dos'),(3, 'Tres'))
thallium_scan_results_choices = ((3, 'Normal'),(6, 'Defecto Fijo'),(7, 'Defecto Reversible'))

class Patient(models.Model):
    medic = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)  
    id_num = models.IntegerField(default=1000000)  
    phone_number = models.IntegerField()
    
    date_of_birth = models.DateField(default=timezone.now)
    age = models.IntegerField(default=20)
    is_active = models.BooleanField(default=True) 
    
    sex = models.IntegerField(choices=sex_choices, default=0)
    cp = models.IntegerField(choices=cp_choice,default=0)
    resting_bp = models.IntegerField()
    serum_cholesterol = models.IntegerField()
    cholesterol_reference_value = models.IntegerField(default=200)
    fasting_blood_sugar = models.IntegerField(choices=fasting_blood_sugar_choices,default=0)
    resting_ecg = models.IntegerField(choices=resting_ecg_choices,default=0)
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.IntegerField(choices=exercise_induced_angina_choices,default=0)
    st_depression = models.DecimalField(max_digits=4, decimal_places=2)
    st_slope = models.IntegerField(choices=st_slope_choices)
    number_of_vessels = models.IntegerField(choices=number_of_vessels_choices)
    thallium_scan_results = models.IntegerField(choices=thallium_scan_results_choices)
    
    predicted = models.BooleanField(default=False)
    predicted_date = models.DateTimeField(default=timezone.now)
    num = models.IntegerField(blank=True, null=True)