from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('examevent/', views.examevent, name='examevent'),

    # signup & signin views
    path('signIn/', views.signInView, name='signIn'),
    path('logout/', views.logoutView, name='logout'),
    path('signUpStudent/', views.signUpStudent, name='signUpStudent'),
    path('signUpQuestionSetter/', views.signUpQuestionSetter, name='signUpQuestionSetter'),
    path('signUpAdmin/', views.signUpAdmin, name='signUpAdmin'),

]
