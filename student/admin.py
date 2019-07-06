from django.contrib import admin
from .models import *


# Register your models here.
class StudentDetailInfoAdmin(admin.ModelAdmin):
    list_display = ('roll', 'std_class')


admin.site.register(StudentInfo)
admin.site.register(StudentShiftInfo)
admin.site.register(StudentClassInfo)
admin.site.register(StudentDetailInfo, StudentDetailInfoAdmin)
admin.site.register(Attendance)
admin.site.register(Result)
