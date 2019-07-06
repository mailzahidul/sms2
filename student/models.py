from django.db import models
from teachers.models import TecherInfo


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=50)
    std_section = models.CharField(max_length=50)

    def __str__(self):
        return self.shift_name


class StudentClassInfo(models.Model):
    class_name = models.CharField(max_length=50)
    class_short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.class_name


class StudentInfo(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    address = models.TextField()
    reference_teacher = models.ForeignKey(TecherInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentDetailInfo(models.Model):
    roll = models.IntegerField()
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    std_class = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    std_shift = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['roll', 'std_class']

    def __str__(self):
        return self.student.name


class AttendanceManager(models.Manager):
    def create_attendance(self, std_cls, std_roll):
        std_obj = StudentDetailInfo.objects.get(
            roll=std_roll,
            std_class__class_short_form=std_cls
        )
        attend_obj = Attendance.objects.create(student=std_obj, status=1)
        return attend_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentDetailInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=3)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return str(self.student.roll)

class Result(models.Model):
    board = models.CharField(max_length=20)
    roll = models.IntegerField()
    gpa = models.FloatField()

    def __str__(self):
        return str(self.roll)
