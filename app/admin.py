from django.contrib import admin

from app.models import myCustomeUser, Student, QuestionSetter, Admin
from app.models import QuestionNumeric, QuestionTureFalse, QuestionSet, StudentAnsNumeric, StudentAnsTureFalse, StudentAnsSet, ExamParticipent
from app.models import Notice, Resource

# User Models...
admin.site.register(myCustomeUser)
admin.site.register(Student)
admin.site.register(QuestionSetter)
admin.site.register(Admin)

# Exam Releted Models...
admin.site.register(QuestionNumeric)
admin.site.register(QuestionTureFalse)
admin.site.register(QuestionSet)
admin.site.register(StudentAnsNumeric)
admin.site.register(StudentAnsTureFalse)
admin.site.register(StudentAnsSet)
admin.site.register(ExamParticipent)


# Others Models...
admin.site.register(Notice)
admin.site.register(Resource)
