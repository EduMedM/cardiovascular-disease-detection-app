from django.urls import path
from prediction import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_medic/<medic_id>', views.edit_medic, name="edit_medic"),
    path('hide_patient/<int:patient_id>', views.hide_patient, name="hide_patient"),
    path('predict_patient/<patient_id>', views.predict_patient, name="predict_patient"),
    path('stats/<patient_id>', views.stats_patient, name="stats_patient"),
]