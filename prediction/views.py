import csv,io
import sklearn
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from prediction.data_provider import *
from prediction.models import Patient
from prediction.forms import PatientForm
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from prediction.forms import UserUpdateForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password
from datetime import date

@login_required
def index(request):
    if not request.user.is_staff:
        print("Get table")
        all_patients = Patient.objects.filter(medic=request.user)

        search_query = request.GET.get('search')
        print(f"search_query {search_query}")

        if search_query:
            all_patients = all_patients.filter(Q(name__icontains=search_query) | 
                                                Q(surname__icontains=search_query)|
                                                Q(id_num__icontains=search_query))

        paginator = Paginator(all_patients, 7)
        page = request.GET.get('pag')
        all_patients = paginator.get_page(page)
        return render(request, "index.html", {'all_patients': all_patients, 'search_query': search_query})
    else:
        return redirect('restricted.html')    


@login_required
def index_medics(request):
    all_medics = User.objects.all()
    
    search_query = request.GET.get('search')
    print(f"search_query {search_query}")

    if search_query:
        all_medics = all_medics.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
    
    paginator = Paginator(all_medics, 7)
    page = request.GET.get('pag')
    all_medics = paginator.get_page(page)
    print(all_medics)
    return render(request, "index_medics.html", {'all_medics': all_medics, 'search_query': search_query})


@login_required
def add(request):
    if not request.user.is_staff:
        if request.method == "POST":
            form = PatientForm(request.POST or None)
            print(request.POST)
            print('post del formulario ADD')
            if form.is_valid():
                instance = form.save(commit=False)
                instance.medic = request.user
                instance.save()
                instance = predict_patient(request, instance.id)
                instance.save()

                return stats_patient(request, instance.id)
            else:
                print('El formulario no es válido')
                print(form.errors)
                print('------------Form Errors------------')
                print(form)
                return redirect('index')
        else:
            form = PatientForm()
            print('instancia de form nueva creada')
        return render(request, 'add.html', {'form': form})
    else:
        return redirect('index')
    
    
@login_required
def predict_patient(request, patient_id):
    predicted = False
    predictions = {}
    patient_obj = Patient.objects.get(pk=patient_id)
    
    if patient_obj.medic == request.user:
        
        st_depression_float = float(patient_obj.st_depression)
        print("st_depression_float: " + str(st_depression_float))
        
        print("Calculando edad: ")
        today = date.today()
        print(f"today: {today}")
        birth_date = patient_obj.date_of_birth
        print(f"birth_date: {birth_date}")
        patient_obj.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"patient_obj.age : {patient_obj.age }")
        print("Calculated age:", patient_obj.age)
        
        features = [[
            patient_obj.age, patient_obj.sex, patient_obj.cp, patient_obj.resting_bp,
            patient_obj.serum_cholesterol, patient_obj.fasting_blood_sugar,
            patient_obj.resting_ecg, patient_obj.max_heart_rate,
            patient_obj.exercise_induced_angina, st_depression_float,
            patient_obj.st_slope, patient_obj.number_of_vessels,
            patient_obj.thallium_scan_results
        ]]

        print("Before scaler",features)
        standard_scaler = get_standard_scaler()
        features = standard_scaler.transform(features)
        print("After scaler",features)
        SVCClassifier, LogisticRegressionClassifier, NaiveBayesClassifier, DecisionTreeClassifier, NeuralNetworkClassifier, KNNClassifier = get_all_classifiers()

        predictions = {'SVC': str(SVCClassifier.predict(features)[0]),
            'LogisticRegression': str(LogisticRegressionClassifier.predict(features)[0]),
             'NaiveBayes': str(NaiveBayesClassifier.predict(features)[0]),
             'DecisionTree': str(DecisionTreeClassifier.predict(features)[0]),
              'NeuralNetwork': str(NeuralNetworkClassifier.predict(features)[0]),
              'KNN': str(KNNClassifier.predict(features)[0]),
              }
        
        results_predictions = [predictions['SVC'], 
            predictions['LogisticRegression'],
            predictions['NaiveBayes'],
            predictions['DecisionTree'],
            predictions['NeuralNetwork'],
            predictions['KNN']]
        
        print(f"Valores de las predicciones: {results_predictions}")
        count = results_predictions.count('1')
        result = False
        
        if count >= 3:
            print(f'El paciente {patient_obj.name} tiene enfermedad cardiaca')
            result = True
            patient_obj.num = 1
            patient_obj.predicted = True
        else:
            print(f'El paciente {patient_obj.name} NO tiene enfermedad cardiaca')
            patient_obj.predicted = True
            patient_obj.num = 0
        
        predicted = True
        patient_obj.save()

        if predicted:
            print("Se hizo la predicción")
        else:
            print("No se hizo la predicción")
        
        return patient_obj


@login_required
def edit_medic(request, medic_id):
    medic_obj = User.objects.get(pk=medic_id)
    form = UserUpdateForm(instance=medic_obj)
    error_message = None

    if request.method == "POST":
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 == password2:
            if password1:
                new_password = make_password(password1)
                print(f'new password entered: {password1}')
                print(f'new password (hash): {new_password}')
                medic_obj.set_password(password1)

            form = UserUpdateForm(request.POST or None, instance=medic_obj)

            if form.is_valid():
                form.save()
                return redirect('index_medics')
        else:
            error_message = "Las contraseñas no coinciden. Inténtalo de nuevo."

    return render(request, 'edit_medic.html', {'medic_obj': medic_obj, 'form': form, 'error_message': error_message})


@login_required
def hide_patient(request, patient_id):
    print('Procesando solicitud para hide_patient')
    if request.method == 'POST':
        patient_obj = Patient.objects.get(pk=patient_id)
        print(f'Ocultando a {patient_obj} / {patient_obj.name}')
        if patient_obj.medic == request.user:
            patient_obj.is_active = False
            patient_obj.save() 
        else:
            messages.error(request, "Acceso Restringido.")
        return redirect('index')


@login_required
def stats_patient(request, patient_id):
    patient_obj = Patient.objects.get(pk=patient_id)
    standard_max_heart_rate = 220 - patient_obj.age
    return render(request, 'stats.html', {'patient_obj': patient_obj, 'standard_max_heart_rate':standard_max_heart_rate})
