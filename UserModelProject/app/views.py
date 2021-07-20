from django.shortcuts import render
from datetime import datetime
from django.utils import timezone

# Create your views here.
from app.models import Student, Teacher
from app.models import questionNumeric, questionTureFalse, questionSet, studentAnsNumeric, studentAnsTureFalse, studentAnsSet, examParticipent


from django.template.defaulttags import register

@register.filter
def get_range(value):
    value = int(value)
    return range(value)


def index(request):
    index_dict = {
    }
    return render(request, 'app/index.html', index_dict)


def examSetting(request):
    examSetting_dict = {
        'Teacher' : Teacher.objects.order_by('id')
    }
    return render(request, 'app/examSetting.html', examSetting_dict)


def quesSetting(request):
    if request.method == "POST":
        this_examName = request.POST['examName']
        # time formating changing
        this_startingTime = request.POST['startingTime']
        this_startingTime = this_startingTime.strip('“”')
        this_startingTime = datetime.strptime(this_startingTime, "%m/%d/%Y %I:%M %p")

        this_durationInMinits = request.POST['durationInMinits']
        questionSetter_pk = request.POST['questionSetter']
        this_questionSetter = Teacher.objects.filter(id = questionSetter_pk).first()
        print(this_questionSetter)

        this_totalMarks = request.POST['totalMarks']
        this_noNumeric = request.POST['noNumeric']
        this_noTureFalse = request.POST['noTureFalse']

        questionSet_obj = questionSet.objects.create(
            examName = this_examName,
            startingTime = this_startingTime,
            durationInMinits = this_durationInMinits,
            questionSetter = this_questionSetter,
            totalMarks = this_totalMarks,
            noNumeric = this_noNumeric,
            noTureFalse = this_noTureFalse
        )
        questionSet_obj.save()

    quesSetting_dict = {
        'questionSet_pk' : questionSet_obj.pk,
        'examName' : this_examName,
        'noNumeric' : questionSet_obj.noNumeric,
        'noTureFalse' : questionSet_obj.noTureFalse,
    }
    return render(request, 'app/quesSetting.html', quesSetting_dict)


def quesSubmittign(request,pk):
    questionSet_obj = questionSet.objects.filter(id = pk).first()
    noNumeric = questionSet_obj.noNumeric
    noTureFalse = questionSet_obj.noTureFalse

    if request.method == "POST":

        # numeric adding question portion
        numericQuestion_list = request.POST.getlist('numericQuestion')
        numericMarks_list = request.POST.getlist('numericMarks')
        numericCorrectAns_list = request.POST.getlist('numericCorrectAns')
        for i in range(noNumeric):
            this_question = numericQuestion_list[i]
            this_marks = numericMarks_list[i]
            this_correctAns = numericCorrectAns_list[i]

            questionNumeric_obj = questionNumeric.objects.create(
                question=this_question,
                marks=this_marks,
                correctAns=this_correctAns
            )
            questionNumeric_obj.save()
            questionSet_obj.questionNumeric.add(questionNumeric_obj)

            # true False ques ans addding
            tureFalseQuestion_list = request.POST.getlist('tureFalseQuestion')
            tureFalseMarks_list = request.POST.getlist('tureFalseMarks')
            tureFalseCorrectAns_list = request.POST.getlist('tureFalseCorrectAns')
            for i in range(noTureFalse):
                this_question = tureFalseQuestion_list[i]
                this_marks = tureFalseMarks_list[i]
                this_correctAns = tureFalseCorrectAns_list[i]

                questionTureFalse_obj = questionTureFalse.objects.create(
                    question=this_question,
                    marks=this_marks,
                    correctAns=this_correctAns
                )
                questionTureFalse_obj.save()
                questionSet_obj.questionTureFalse.add(questionTureFalse_obj)

    print(questionSet_obj)
    quesSubmittign_dict = {

    }
    return render(request, 'app/quesSubmittign.html', quesSubmittign_dict)







'''
sundayRoutine_obj = sundayRoutine.objects.order_by('id')

for i in sundayRoutine_obj:
    startingTime = i.startingHour
    durationInMinits = i.durationInMinits
    if(startingTime <= timezone.now() < startingTime + timezone.timedelta(minutes=durationInMinits)):
        print(startingTime)
        print(" is Running")
    else:
        print(startingTime)
        print(" is Not Running")

'''
