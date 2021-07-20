from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('examSetting/', views.examSetting, name='examSetting'),
    path('quesSetting/', views.quesSetting, name='quesSetting'),
    path('quesSubmittign/<int:pk>/', views.quesSubmittign, name='quesSubmittign'),

]
