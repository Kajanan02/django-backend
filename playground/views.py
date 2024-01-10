from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from playground.serializers import MovieSerializer
from playground.models import Movie

@csrf_exempt
def MovieApi(request,id=0):
    if request.method=='GET':
        movie = Movie.objects.all()
        print(movie)
        movie_serializer=MovieSerializer(movie,many=True)
        return JsonResponse(movie_serializer.data,safe=False)
    elif request.method=='POST':
        movie_data=JSONParser().parse(request)
        movie_serializer=MovieSerializer(data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        movie_data=JSONParser().parse(request)
        movie=Movie.objects.get(id=id)
        movie_serializer=MovieSerializer(movie,data=movie_data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return JsonResponse("Deleted Successfully",safe=False)
