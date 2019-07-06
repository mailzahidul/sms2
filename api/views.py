from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from student.models import Attendance, StudentDetailInfo, Result
from .serializers import ResultSerializer


# Create your views here.
# @api_view()
# def std_attendance(request, std_cls, std_roll):
#     try:
#         Attendance.objects.create_attendance(std_cls, std_roll)
#         return Response({'status': 'success'}, status=status.HTTP_200_OK)
#     except Exception as err:
#         print(err)
#         return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class StudentAttendance(APIView):
    def get(self, request, std_cls, std_roll):
        try:
            Attendance.objects.create_attendance(std_cls, std_roll)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)


class ResultViews(APIView):
    def post(self, request):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.validated_data['board']
            roll = serializer.validated_data['roll']
            result_obj = Result.objects.get(board=board, roll=roll)
            return Response({'Result: ': result_obj.gpa}, status=status.HTTP_200_OK)
        return Response(request.errors, status=status.HTTP_200_OK)
