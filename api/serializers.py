from rest_framework import serializers
from .models import Faculty, Staff, Event, gallery , Feed

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name', 'image', 'email', 'phoneno', 'post', 'interest_area_1', 'interest_area_2', 'joined_year']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['id', 'name', 'image', 'email', 'phoneno', 'post', 'interest_area_1', 'interest_area_2', 'joined_year']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'EventName', 'Date', 'Link', 'EventType']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = ['id', 'Image']

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['id', 'name','link','date']
