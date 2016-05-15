from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from techson_server.settings import BASE_DIR
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.contrib.auth.models import User
from api.serializers import UserSerializer, InputDataSerializer, ImageSerializer
from api.models import Image
from techson_server.settings import MEDIA_ROOT, UPLOAD_FILE_TYPES

import pickle, json, os, random, string


# Create your views here.

@api_view(['POST'])
def random_forest(request):
    path = BASE_DIR + "/classifiers/random_forest_classifier.pkl"
    with open(path, 'rb') as f:
        classifier = pickle.load(f)
    data = request.data['image'].split(",")
    predict = classifier.predict_proba(data)[0]
    keys = list(range(10))
    result = dict(zip(keys, predict))
    return Response(result)


@api_view(['POST'])
def neural_network(request):
    path = BASE_DIR + "/classifiers/random_forest_classifier.pkl"
    with open(path, 'rb') as f:
        classifier = pickle.load(f)
    data = request.data['image'].split(",")
    predict = classifier.predict_proba(data)[0]
    keys = list(range(10))
    result = dict(zip(keys, predict))
    return Response(result)


@api_view(['POST'])
def gradient_boosting(request):
    path = BASE_DIR + "/classifiers/random_forest_classifier.pkl"
    with open(path, 'rb') as f:
        classifier = pickle.load(f)
    data = request.data['image'].split(",")
    predict = classifier.predict_proba(data)[0]
    keys = list(range(10))
    result = dict(zip(keys, predict))
    return Response(result)


@api_view(['GET'])
def users(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


DIR = os.path.dirname(__file__)


@api_view(['GET'])
def initial_data(request):
    users = []
    with open(os.path.join(DIR, 'users.json'), encoding='utf-8') as data_file:
        json_data = json.load(data_file)
        for data in json_data:
            user, created = User.objects.get_or_create(username=data['username'], defaults=data)
            users.append(user)
    serializer = UserSerializer(users, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def load_image(request):
    input_data = InputDataSerializer(data=request.data)
    input_data.is_valid(raise_exception=True)
    try:

        file_obj = request.FILES['image']
        file_extension = validate_file(file_obj)
        dir_path = get_or_create_dir(input_data.data['label'])

        old_name = file_obj.name
        new_name = create_random_name(file_extension)

        file_path = dir_path + "/" + new_name

        with open(file_path, "wb") as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        destination.close()

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, id=input_data.data['user'])

    image = Image.objects.create(user=user, label=input_data.data['label'],
                                 new_name=new_name, old_name=old_name,
                                 image=file_path, data=input_data.data['data'])

    return Response(ImageSerializer(image).data)


def get_or_create_dir(label):
    if not os.path.exists(MEDIA_ROOT):
        os.makedirs(MEDIA_ROOT)
    dir_path = MEDIA_ROOT + "/" + str(label)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def create_random_name(file_extension):
    s = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(50))
    s += '.' + file_extension
    return s


def validate_file(file_obj):
    file_type = file_obj.name.split('.')
    if len(file_type) == 1:
        raise exceptions.ValidationError('File without type is not supported')

    file_type = file_type[len(file_type) - 1]

    if str.lower(str(file_type)) in UPLOAD_FILE_TYPES:
        pass
    else:
        raise exceptions.ValidationError("File type '.%s' is not supported" % file_type)
    return file_type
