from django.urls import path

from backend.exam import views as v

app_name = 'exam'

urlpatterns = [
    path('', v.care_list, name='care_list'),
    path('create/', v.care_create, name='care_create'),
    path('<int:pk>/', v.care_detail, name='care_detail'),
    path('<int:pk>/update/', v.care_update, name='care_update'),
    path('<int:pk>/update/exam/', v.care_update_exam, name='care_update_exam'),
]
