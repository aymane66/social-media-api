from django.urls import path
from .views import NotificationListView, MarkNotificationReadView


urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='mark-read'),
]
