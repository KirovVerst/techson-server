from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name')


class InputDataSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    label = serializers.IntegerField(min_value=0, max_value=9)
    image = serializers.FileField()
    data = serializers.CharField()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
