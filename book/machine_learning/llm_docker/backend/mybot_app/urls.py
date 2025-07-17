from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('mattermost/webhook/', views.mattermost_webhook, name='mattermost_webhook'),
    path('api/query/', views.query_view, name='query'),
]