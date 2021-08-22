from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
import datetime
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

from app.models import myCustomeUser, Student, QuestionSetter, Admin
from app.models import QuestionNumeric, QuestionTureFalse, QuestionSet, StudentAnsNumeric, StudentAnsTureFalse, StudentAnsSet, ExamParticipent
from app.models import Notice, Resource
from app.decorators import studentRequired, questionSetterRequired, adminRequired


# General Pages Views
def index(request):
    return render(request, 'app/index.html')

def examevent(request):
    QuestionSet_obj = QuestionSet.objects.filter(isCompleted=False)
    examevent_dict={
        "QuestionSet_obj" : QuestionSet_obj,
        'currentTime' : datetime.datetime.now(),
        'startingTime' : datetime.datetime.now(),
    }
    return render(request, 'app/examevent.html', examevent_dict)


def notice(request):
    list = Notice.objects.order_by('-id')
    if request.method == "POST":
        this_user = myCustomeUser.objects.get(username=request.user.username)
        this_topic = request.POST['topic']
        this_details = request.POST['details']
        Notice_obj = Notice.objects.create(
            user = this_user,
            topic=this_topic,
            details=this_details
        )
        Notice_obj.save()
    notice_dict={
        'list' : list
    }
    return render(request, 'app/notice.html', notice_dict)


def resource(request):
    list = Resource.objects.order_by('-id')
    if request.method == "POST":
        this_user = myCustomeUser.objects.get(username=request.user.username)
        this_topic = request.POST['topic']
        this_details = request.POST['details']
        this_link = request.POST['link']
        Resource_obj = Resource.objects.create(
            user = this_user,
            topic=this_topic,
            details=this_details,
            link=this_link
        )
        Resource_obj.save()
    resource_dict={
        'list' : list
    }
    return render(request, 'app/resource.html', resource_dict)


def ourTeam(request):
    QuestionSetter_obj = QuestionSetter.objects.all()
    Student_obj = Student.objects.all()
    Admin_obj = Admin.objects.all()

    ourTeam_dict = {
        'QuestionSetter_obj' : QuestionSetter_obj,
        'Student_obj' : Student_obj,
        'Admin_obj' : Admin_obj,
    }
    return render(request, 'app/ourTeam.html', ourTeam_dict)




def fourZeroFour(request):
    return render(request, 'app/fourZeroFour.html')

def my404(request, exception):
    return render(request, 'app/fourZeroFour.html')

def examforbidden(request):
    return render(request, 'app/examforbidden.html')

def examSuccess(request):
    return render(request, 'app/examSuccess.html')

def loginFromCorrectAccount(request):
    return render(request, 'app/loginFromCorrectAccount.html')


def result(request):
    Result_obj = QuestionSet.objects.filter(isCompleted=True)
    result_dict = {
        'Result_obj' : Result_obj,
    }
    return render(request, 'app/result.html', result_dict)



def resultSingle(request, questionsetpk):
    Question_obj = QuestionSet.objects.get(id=questionsetpk)
    StudentAnsSet_obj = StudentAnsSet.objects.filter(questionSet=Question_obj)
    resultSingle_dict = {
        'Question_obj' : Question_obj,
        'Result_obj' : StudentAnsSet_obj,
    }

    return render(request, 'app/resultSingle.html', resultSingle_dict)

def StudentIndividualAnsSheet(request, anssetpk):
    StudentAnsSet_obj = StudentAnsSet.objects.get(id=anssetpk)
    Student_obj = Student.objects.get(user=StudentAnsSet_obj.student.user)

    StudentIndividualAnsSheet_dict = {
        'StudentAnsSet_obj' : StudentAnsSet_obj,
        'Student_obj' : Student_obj,
    }

    return render(request, 'app/StudentIndividualAnsSheet.html', StudentIndividualAnsSheet_dict)







# login, Logout, Register & Profile Redirect Views
def signInView(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        user = authenticate(username=this_username, password=plain_password)
        if user is not None:
            login(request, user)
            if user.isStudent == True:
                return redirect('app:examevent')
            elif user.isQuestionSetter == True:
                return redirect('app:questionSetterProfile')
            elif user.isAdmin == True:
                return redirect('app:adminProfile')
    return redirect('app:index')


def logoutView(request):
    logout(request)
    return redirect('app:index')


def signUpStudent(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_studentID = request.POST['studentID']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isStudent=True
            )
            Student_obj = Student.objects.create(
                user=u, name=this_name, email=this_email, studentID=this_studentID
            )
            Student_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:index')

    return render(request, 'app/signUpStudent.html')


def signUpQuestionSetter(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_rank = request.POST['rank']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isQuestionSetter=True
            )
            QuestionSetter_obj = QuestionSetter.objects.create(
                user=u, name=this_name, email=this_email, rank=this_rank
            )
            QuestionSetter_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:questionSetterProfile')

    return render(request, 'app/signUpQuestionSetter.html')


def signUpAdmin(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isAdmin=True
            )
            Admin_obj = Admin.objects.create(
                user=u, name=this_name, email=this_email
            )
            Admin_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:index')

    return render(request, 'app/signUpAdmin.html')


def redirectToProfile(request):
    user = request.user
    if user is not None:
        if user.isStudent == True:
            return redirect('app:examevent')
        elif user.isQuestionSetter == True:
            return redirect('app:questionSetterProfile')
        elif user.isAdmin == True:
            return redirect('app:adminProfile')
    return redirect('app:index')





# Admins View
@adminRequired
def adminProfile(request):
    adminProfile_obj = Admin.objects.get(user=request.user)
    QuestionSetter_obj = QuestionSetter.objects.all()
    Student_obj = Student.objects.all()
    Admin_obj = Admin.objects.all()
    adminProfile_dict = {
        'adminProfile_obj' : adminProfile_obj,
        'QuestionSetter_obj' : QuestionSetter_obj,
        'Student_obj' : Student_obj,
        'Admin_obj' : Admin_obj,
    }
    return render(request,'app/adminProfile.html', adminProfile_dict)

@adminRequired
def ApproveQuestionSetter(request, pk):
    QuestionSetter_obj = QuestionSetter.objects.get(id=pk)
    QuestionSetter_obj.isVarified = True
    QuestionSetter_obj.save()
    return redirect('app:adminProfile')

@adminRequired
def RemoveApprovalQuestionSetter(request, pk):
    QuestionSetter_obj = QuestionSetter.objects.get(id=pk)
    QuestionSetter_obj.isVarified = False
    QuestionSetter_obj.save()
    return redirect('app:adminProfile')

@adminRequired
def DeleteQuestionSetter(request, pk):
    QuestionSetter_obj = QuestionSetter.objects.get(id=pk)
    QuestionSetter_obj.delete()
    return redirect('app:adminProfile')

@adminRequired
def DeleteStudent(request, pk):
    Student_obj = Student.objects.get(id=pk)
    Student_obj.delete()
    return redirect('app:adminProfile')



#Question setter's Views
@questionSetterRequired
def questionSetterProfile(request):

    QuestionSetter_obj = QuestionSetter.objects.get(user=request.user)
    criterion1 = Q(questionSetter=QuestionSetter_obj)
    criterion2 = Q(isCompleted=False)
    criterion3 = Q(isCompleted=True)
    QuestionSet_obj = QuestionSet.objects.filter(criterion1 & criterion2)
    TakenQuestionSet_obj = QuestionSet.objects.filter(criterion1 & criterion3)

    questionSetterProfile_dict = {
        'QuestionSetter_obj' : QuestionSetter_obj,
        'QuestionSet_obj' : QuestionSet_obj,
        'TakenQuestionSet_obj' : TakenQuestionSet_obj,
    }

    if request.method == 'POST':
        this_examName = request.POST['examName']
        this_topic = request.POST['topic']
        this_description = request.POST['description']
        this_totalMarks = 0
        this_submissionTimeLimit = request.POST['submissionTimeLimit']
        this_startingTime = request.POST['startingTime']
        this_durationInMinits = request.POST['durationInMinits']
        this_multipleSubmission = request.POST['multipleSubmission']

        QuestionSet_obj = QuestionSet.objects.create(
            examName = this_examName,
            topic = this_topic,
            description = this_description,
            totalMarks = this_totalMarks,
            submissionTimeLimit = this_submissionTimeLimit,
            startingTime = this_startingTime,
            durationInMinits = this_durationInMinits,
            questionSetter = QuestionSetter_obj,
            multipleSubmission = this_multipleSubmission

        )
        QuestionSet_obj.save()
        mypk = QuestionSet_obj.pk
        return redirect('app:QuestionSetting', pk=mypk)

    return render(request,'app/questionSetterProfile.html', questionSetterProfile_dict)



@questionSetterRequired
def QuestionSetting(request, pk):
    QuestionSetter_obj = QuestionSetter.objects.get(user=request.user)
    QuestionSet_obj = QuestionSet.objects.get(id=pk)

    QuestionSetting_dict = {
        'QuestionSetter_obj' : QuestionSetter_obj,
        'QuestionSet_obj' : QuestionSet_obj,
    }
    if QuestionSetter_obj == QuestionSet_obj.questionSetter:
        return render(request,'app/QuestionSetting.html', QuestionSetting_dict)
    else:
        return redirect('app:fourZeroFour')


@questionSetterRequired
def ReleseExam(request, pk):
    QuestionSet_obj = QuestionSet.objects.get(id=pk)
    QuestionSet_obj.isCompleted = True
    QuestionSet_obj.save()
    return redirect('app:questionSetterProfile')


@questionSetterRequired
def DeleteExam(request, pk):
    QuestionSet_obj = QuestionSet.objects.get(id=pk)
    QuestionSet_obj.delete()
    return redirect('app:questionSetterProfile')



@questionSetterRequired
def DeleteNumericQuestion(request, pk):
    QuestionNumeric_obj = QuestionNumeric.objects.get(id=pk)
    Question_set = QuestionSet.objects.filter(questionNumeric=QuestionNumeric_obj).first()
    QuestionNumeric_obj.delete()
    mypk = Question_set.pk
    return redirect('app:QuestionSetting', pk=mypk)

@questionSetterRequired
def DeleteTrueFalseQuestion(request, pk):
    QuestionTureFalse_obj = QuestionTureFalse.objects.get(id=pk)
    Question_set = QuestionSet.objects.filter(questionTureFalse=QuestionTureFalse_obj).first()
    QuestionTureFalse_obj.delete()
    mypk = Question_set.pk
    return redirect('app:QuestionSetting', pk=mypk)


@questionSetterRequired
def AddTrueFalseQuestion(request, questionsetpk):
    QuestionSetter_obj = QuestionSetter.objects.get(user=request.user)
    QuestionSet_obj = QuestionSet.objects.get(id=questionsetpk)

    if QuestionSetter_obj == QuestionSet_obj.questionSetter:
        if request.method == 'POST':
            this_question = request.POST['question']
            this_correctAns = request.POST['correctAns']
            this_marks = int(request.POST['marks'])

            QuestionTureFalse_obj = QuestionTureFalse.objects.create(
                question = this_question,
                correctAns = this_correctAns,
                marks = this_marks,
            )
            QuestionTureFalse_obj.save()
            QuestionSet_obj.questionTureFalse.add(QuestionTureFalse_obj)
            QuestionSet_obj.totalMarks = QuestionSet_obj.totalMarks + this_marks
            QuestionSet_obj.save()
            return redirect('app:QuestionSetting', questionsetpk)
    else:
        return redirect('app:fourZeroFour')


@questionSetterRequired
def AddNumericQuestion(request, questionsetpk):
    QuestionSetter_obj = QuestionSetter.objects.get(user=request.user)
    QuestionSet_obj = QuestionSet.objects.get(id=questionsetpk)

    if QuestionSetter_obj == QuestionSet_obj.questionSetter:
        if request.method == 'POST':
            this_question = request.POST['question']
            this_correctAns = request.POST['correctAns']
            this_marks = int(request.POST['marks'])

            QuestionNumeric_obj = QuestionNumeric.objects.create(
                question = this_question,
                correctAns = this_correctAns,
                marks = this_marks,
            )
            QuestionNumeric_obj.save()
            QuestionSet_obj.questionNumeric.add(QuestionNumeric_obj)
            QuestionSet_obj.totalMarks = QuestionSet_obj.totalMarks + this_marks
            QuestionSet_obj.save()
            return redirect('app:QuestionSetting', questionsetpk)
    else:
        return redirect('app:fourZeroFour')



@studentRequired
def Exam(request, questionsetpk):
    QuestionSet_obj = QuestionSet.objects.get(id=questionsetpk)
    Student_obj = Student.objects.get(user=request.user)

    QuestionTureFalse_set = QuestionTureFalse.objects.filter(rvsToQues__id=questionsetpk)
    QuestionNumeric_set = QuestionNumeric.objects.filter(rvsToQues__id=questionsetpk)

    criterion1 = Q(student=Student_obj)
    criterion2 = Q(questionSet=QuestionSet_obj)
    CheckExamParticipent = ExamParticipent.objects.filter(criterion1 & criterion2).first()

    Allow_To_Participate_Multiple_Time = QuestionSet_obj.multipleSubmission
    TimeCheck = False

    if QuestionSet_obj.submissionTimeLimit:
        TimeCheck = True
    elif QuestionSet_obj.startingTime <= timezone.now() < QuestionSet_obj.startingTime + timezone.timedelta(minutes=QuestionSet_obj.durationInMinits):
        TimeCheck = True
    else:
        TimeCheck = False


    if (CheckExamParticipent is None) and (TimeCheck):
        StudentAnsSet_obj = StudentAnsSet.objects.create(
            student = Student_obj,
            questionSet = QuestionSet_obj
        )
        StudentAnsSet_obj.save()

        for i in QuestionTureFalse_set:
            StudentAnsTureFalse_obj = StudentAnsTureFalse.objects.create(
                question = i,
                student = Student_obj
            )
            StudentAnsTureFalse_obj.save()
            StudentAnsSet_obj.studentAnsTureFalse.add(StudentAnsTureFalse_obj)
            StudentAnsSet_obj.save()

        for i in QuestionNumeric_set:
            StudentAnsNumeric_obj = StudentAnsNumeric.objects.create(
                question = i,
                student = Student_obj
            )
            StudentAnsNumeric_obj.save()
            StudentAnsSet_obj.studentAnsNumeric.add(StudentAnsNumeric_obj)
            StudentAnsSet_obj.save()

        ExamParticipent_obj = ExamParticipent.objects.create(
            student = Student_obj,
            studentAnsSet = StudentAnsSet_obj,
            questionSet = QuestionSet_obj
        )
        ExamParticipent_obj.save()

        Exam_dict = {
            'QuestionSet_obj' : QuestionSet_obj,
            'Student_obj' : Student_obj,
            'StudentAnsSet_obj' : StudentAnsSet_obj

        }
        return render(request, 'app/Exam.html', Exam_dict)

    elif (Allow_To_Participate_Multiple_Time == True) and TimeCheck:
        StudentAnsSet_obj = StudentAnsSet.objects.filter(rvsToAnsSet__id=CheckExamParticipent.pk).first()
        StudentAnsTureFalse_obj = StudentAnsTureFalse.objects.filter(rvsToAnsSet__id=StudentAnsSet_obj.pk)
        studentAnsNumeric_obj = StudentAnsNumeric.objects.filter(rvsToAnsSet__id=StudentAnsSet_obj.pk)

        Exam_dict = {
            'QuestionSet_obj' : QuestionSet_obj,
            'Student_obj' : Student_obj,
            'ExamParticipent' : CheckExamParticipent,
            'StudentAnsSet_obj' : StudentAnsSet_obj,
            'StudentAnsTureFalse_obj' : StudentAnsTureFalse_obj,
            'studentAnsNumeric_obj' : studentAnsNumeric_obj,

        }
        return render(request, 'app/Exam.html', Exam_dict)

    else:
        return redirect('app:examforbidden')



@studentRequired
def ExamAnsSubmission(request, anssetpk):
    Student_obj = Student.objects.get(user=request.user)
    StudentAnsSet_obj = StudentAnsSet.objects.get(id=anssetpk)
    StudentAnsTureFalse_set = StudentAnsTureFalse.objects.filter(rvsToAnsSet__id=anssetpk)
    StudentAnsNumeric_set = StudentAnsNumeric.objects.filter(rvsToAnsSet__id=anssetpk)
    QuestionSet_obj = StudentAnsSet_obj.questionSet

    totalObtainedMarks = 0
    TimeCheck = False

    if QuestionSet_obj.submissionTimeLimit:
        TimeCheck = True
    elif QuestionSet_obj.startingTime <= timezone.now() < QuestionSet_obj.startingTime + timezone.timedelta(minutes=QuestionSet_obj.durationInMinits):
        TimeCheck = True
    else:
        TimeCheck = False

    if (request.method == 'POST') and TimeCheck:
        for j in StudentAnsTureFalse_set:
            TrueFalseAns_pk = 'TrueFalseAns_' + str(j.pk)
            j.givenAns = request.POST[TrueFalseAns_pk]

            if j.givenAns == str(j.question.correctAns):
                j.obtainedMarks = j.question.marks
                totalObtainedMarks = totalObtainedMarks + j.obtainedMarks
            else:
                j.obtainedMarks = 0
            j.save()

        for j in StudentAnsNumeric_set:
            NumericAns_pk = 'NumericAns_' + str(j.pk)
            j.givenAns = request.POST[NumericAns_pk]

            if float(j.givenAns) == float(j.question.correctAns):
                j.obtainedMarks = j.question.marks
                totalObtainedMarks = totalObtainedMarks + j.obtainedMarks
            else:
                j.obtainedMarks = 0
            j.save()

        StudentAnsSet_obj.totalObtainedMarks = totalObtainedMarks
        StudentAnsSet_obj.submissionTime = datetime.datetime.now()
        StudentAnsSet_obj.save()

        return redirect('app:examSuccess')

    return redirect('app:examforbidden')
