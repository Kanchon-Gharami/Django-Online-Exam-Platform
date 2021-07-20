from django.contrib import admin

from app.models import Student, Teacher

from app.models import questionNumeric, questionTureFalse, questionSet, studentAnsNumeric, studentAnsTureFalse, studentAnsSet, examParticipent
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)

# new models
admin.site.register(questionNumeric)
admin.site.register(questionTureFalse)
admin.site.register(questionSet)
admin.site.register(studentAnsNumeric)
admin.site.register(studentAnsTureFalse)
admin.site.register(studentAnsSet)
admin.site.register(examParticipent)
