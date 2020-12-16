from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mood.models import Mood, Thinker
from mood.serializers import MoodSerializer, ThinkerSerializer

@csrf_exempt
def thinker_list(request):
    if request.method == 'GET':
        thinkers = Thinker.objects.all()
        serializer = ThinkerSerializer(thinkers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ThinkerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def mood_append(request, mood, thinker):
    if request.method == 'GET':
        data = {'mood': mood, 'thinker': thinker}
        serializer = MoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
