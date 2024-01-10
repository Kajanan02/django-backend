from rest_framework import serializers
from playground.models import Movie
from playground.models import Contact
from playground.models import BookingSeat
from playground.models import FAQ


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingSeat
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
