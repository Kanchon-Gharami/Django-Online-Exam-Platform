from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    # General Pages
    path('', views.index, name='index'),
    path('examevent/', views.examevent, name='examevent'),
    path('notice/', views.notice, name='notice'),
    path('resource/', views.resource, name='resource'),
    path('ourTeam/', views.ourTeam, name='ourTeam'),
    path('result/', views.result, name='result'),
    path('resultSingle/<int:questionsetpk>', views.resultSingle, name='resultSingle'),
    path('StudentIndividualAnsSheet/<int:anssetpk>', views.StudentIndividualAnsSheet, name='StudentIndividualAnsSheet'),
    path('fourZeroFour/', views.fourZeroFour, name='fourZeroFour'),
    path('my404/', views.my404, name='my404'),
    path('examforbidden/', views.examforbidden, name='examforbidden'),
    path('examSuccess/', views.examSuccess, name='examSuccess'),
    path('loginFromCorrectAccount/', views.loginFromCorrectAccount, name='loginFromCorrectAccount'),

    # signup & signin views
    path('signIn/', views.signInView, name='signIn'),
    path('logout/', views.logoutView, name='logout'),
    path('signUpStudent/', views.signUpStudent, name='signUpStudent'),
    path('signUpQuestionSetter/', views.signUpQuestionSetter, name='signUpQuestionSetter'),
    path('signUpAdmin/', views.signUpAdmin, name='signUpAdmin'),
    path('redirectToProfile/', views.redirectToProfile, name='redirectToProfile'),

    #Admin Accessed pages
    path('adminProfile/', views.adminProfile, name='adminProfile'),
    path('ApproveQuestionSetter/<int:pk>', views.ApproveQuestionSetter, name='ApproveQuestionSetter'),
    path('RemoveApprovalQuestionSetter/<int:pk>', views.RemoveApprovalQuestionSetter, name='RemoveApprovalQuestionSetter'),
    path('DeleteQuestionSetter/<int:pk>', views.DeleteQuestionSetter, name='DeleteQuestionSetter'),
    path('DeleteStudent/<int:pk>', views.DeleteStudent, name='DeleteStudent'),

    #QuestionSetter Accessed pages
    path('questionSetterProfile/', views.questionSetterProfile, name='questionSetterProfile'),
    path('QuestionSetting/<int:pk>', views.QuestionSetting, name='QuestionSetting'),
    path('ReleseExam/<int:pk>', views.ReleseExam, name='ReleseExam'),
    path('DeleteExam/<int:pk>', views.DeleteExam, name='DeleteExam'),
    path('AddTrueFalseQuestion/<int:questionsetpk>', views.AddTrueFalseQuestion, name='AddTrueFalseQuestion'),
    path('AddNumericQuestion/<int:questionsetpk>', views.AddNumericQuestion, name='AddNumericQuestion'),
    path('DeleteTrueFalseQuestion/<int:pk>', views.DeleteTrueFalseQuestion, name='DeleteTrueFalseQuestion'),
    path('DeleteNumericQuestion/<int:pk>', views.DeleteNumericQuestion, name='DeleteNumericQuestion'),

    #Student Accessed pages
    path('Exam/<int:questionsetpk>', views.Exam, name='Exam'),
    path('ExamAnsSubmission/<int:anssetpk>', views.ExamAnsSubmission, name='ExamAnsSubmission'),

]
