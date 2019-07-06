from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    board = serializers.CharField()
    roll = serializers.IntegerField()
