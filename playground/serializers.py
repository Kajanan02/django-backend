from rest_framework import serializers
from playground.models import Movie
from playground.models import Contact
from playground.models import BookingSeat
from playground.models import FAQ
from playground.models import ROOM
from django.contrib.auth.models import User


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
class ROOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = ROOM
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_superuser', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }
