from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from playground.serializers import MovieSerializer
from playground.serializers import ContactSerializer
from playground.serializers import BookingSerializer
from playground.serializers import FAQSerializer
from playground.serializers import ROOMSerializer
from playground.models import Movie
from playground.models import Contact
from playground.models import BookingSeat
from playground.models import FAQ
from playground.models import ROOM

@csrf_exempt
def MovieApi(request,id=0):
    if request.method=='GET':
        movie = Movie.objects.all()
        # print(movie)
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
        return JsonResponse("Deleted SucceBookingSerializerssfully",safe=False)



@csrf_exempt
def ContactApi(request,id=0):
    if request.method=='GET':
        contact = Contact.objects.all()
        # print(contact)
        contact_serializer=ContactSerializer(contact,many=True)
        return JsonResponse(contact_serializer.data,safe=False)
    elif request.method=='POST':
        contact_data=JSONParser().parse(request)
        contact_serializer=ContactSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def BookingApi(request,id=0):
    if request.method=='GET':
        booking = BookingSeat.objects.all()
        # print(booking)
        booking_serializer=BookingSerializer(booking,many=True)
        return JsonResponse(booking_serializer.data,safe=False)
    elif request.method=='POST':
        booking_data=JSONParser().parse(request)
        booking_serializer=BookingSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def FAQApi(request,id=0):
    if request.method=='GET':
        faq = FAQ.objects.all()
        print(faq)
        faq_serializer=FAQSerializer(faq,many=True)
        return JsonResponse(faq_serializer.data,safe=False)
    elif request.method=='POST':
        faq_data=JSONParser().parse(request)
        faq_serializer=FAQSerializer(data=faq_data)
        if faq_serializer.is_valid():
            faq_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        faq_data=JSONParser().parse(request)
        faq=FAQ.objects.get(id=id)
        faq_serializer=FAQSerializer(faq,data=faq_data)
        if faq_serializer.is_valid():
            faq_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        faq=FAQ.objects.get(id=id)
        faq.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def ROOMSApi(request,id=0):
    if request.method=='GET':
        room = ROOM.objects.all()
        room_serializer=ROOMSerializer(room,many=True)
        return JsonResponse(room_serializer.data,safe=False)
    elif request.method=='POST':
        room_data=JSONParser().parse(request)
        room_serializer=ROOMSerializer(data=room_data)
        if room_serializer.is_valid():
            room_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='DELETE':
        faq=FAQ.objects.get(id=id)
        faq.delete()
        return JsonResponse("Deleted Successfully",safe=False)

