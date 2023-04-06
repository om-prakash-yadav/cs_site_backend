from django.urls import path, include
from . import views

urlpatterns = [
    path('faculty/', views.FacultyList.as_view(), name='faculty-list'),
    path('staff/', views.StaffList.as_view(), name='staff-list'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('gallery/', views.GalleryList.as_view(), name='gallery-list'),
    path('feed/', views.FeedList.as_view(), name='feed-list'),
]
