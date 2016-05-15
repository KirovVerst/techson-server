from rest_framework.decorators import api_view
from techson_server.settings import BASE_DIR
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from api.serializers import UserSerializer
import pickle, json, os


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
    try:
        with open(os.path.join(DIR, 'users.json'), encoding='utf-8') as data_file:
            json_data = json.load(data_file)
            for data in json_data:
                user, created = User.objects.get_or_create(username=data['username'], defaults=data)
                users.append(user)
        serializer = UserSerializer(users, many=True)
    except Exception:
        return Response("File not found.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
