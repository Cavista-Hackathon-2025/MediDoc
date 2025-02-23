from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import google_login, google_callback, create_calendar_event, get_upcoming_events

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user', views.user_logout, name='logout'),
    path('', views.index, name='landing_page'),
    path('google/auth/', google_login, name='google_auth'),
    path('google/callback/', google_callback, name='google_callback'),
    path('calendar/create/', create_calendar_event, name='create_event'),
    path('calendar/events/', get_upcoming_events, name='get_upcoming_events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)