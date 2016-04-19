from rest_framework.decorators import api_view
from techson_server.settings import BASE_DIR
from rest_framework.response import Response
import pickle, json


# Create your views here.

@api_view(['POST'])
def run(request):
    path = BASE_DIR + "/random_forest/classifier.pkl"
    with open(path, 'rb') as f:
        classifier = pickle.load(f)
    data = request.data['image'].split(",")
    predict = classifier.predict_proba(data)[0]
    keys = list(range(10))
    result = dict(zip(keys, predict))
    return Response(result)
