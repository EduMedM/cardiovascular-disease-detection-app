from django.contrib import admin
from django.urls import path, include
from prediction import views as prediction_views
from users_app.views import register

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', register, name="register"),
    path('prediction/', include('prediction.urls')),
    path('users_app', include('users_app.urls')),
    path('', prediction_views.index, name='index'),
    path('account/', include('users_app.urls')),
    path('add/', prediction_views.add, name='add'),
    path('medics/', prediction_views.index_medics, name='index_medics'),
]
