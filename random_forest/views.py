from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from techson_server.settings import BASE_DIR
import pickle


# Create your views here.

@api_view(['POST'])
def run(request):
    path = BASE_DIR + "/random_forest/classifier.pkl"
    with open(path, 'rb') as f:
        classifier = pickle.load(f)
    data = request.data['image'].split(",")
    predict = classifier.predict(data)[0]
    return JsonResponse(str(predict), safe=False)
