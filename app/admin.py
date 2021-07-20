from django.contrib import admin

from app.models import myCustomeUser, Student, QuestionSetter, Admin

# Register your models here.

admin.site.register(myCustomeUser)
admin.site.register(Student)
admin.site.register(QuestionSetter)
admin.site.register(Admin)
