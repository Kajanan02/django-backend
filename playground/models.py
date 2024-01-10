from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=900)
    description = models.TextField(max_length=2000, null=True, blank=True)
    image = models.TextField(max_length=900, null=True, blank=True)
    imageBanner = models.TextField(max_length=900, null=True, blank=True)
    category = models.TextField(max_length=900, null=True, blank=True)
    actor = models.TextField(max_length=1500, null=True, blank=True)
    genre = models.TextField(max_length=900, null=True, blank=True)
    release = models.TextField(max_length=900, null=True, blank=True)
    language = models.TextField(max_length=900, null=True, blank=True)
    rate = models.TextField(max_length=900, null=True, blank=True)
    fee = models.TextField(max_length=900, null=True, blank=True)
    duration = models.TextField(max_length=900, null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=900)
    email = models.TextField(max_length=2000, null=True, blank=True)
    contactNo = models.TextField(max_length=2000, null=True, blank=True)
    subject = models.TextField(max_length=5000, null=True, blank=True)
    message = models.TextField(max_length=900, null=True, blank=True)


class BookingSeat(models.Model):
    name = models.TextField(max_length=900, null=True, blank=True)
    email = models.TextField(max_length=900, null=True, blank=True)
    contactNo = models.TextField(max_length=900, null=True, blank=True)
    address = models.TextField(max_length=900, null=True, blank=True)
    seats = models.JSONField(null=True, blank=True)
    movieName = models.TextField(max_length=900, null=True, blank=True)
    movieDate = models.TextField(max_length=900, null=True, blank=True)
    movieTime = models.TextField(max_length=900, null=True, blank=True)

class FAQ(models.Model):
    question = models.TextField(max_length=900, null=True, blank=True)
    answer = models.TextField(max_length=900, null=True, blank=True)

