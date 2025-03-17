from django.urls import path
from . import views

# Define url patterns here
urlpatterns = [
    path('user/<str:id>/notes', views.getNotes),
    path('user/create', views.createNote),
    path('user/<str:user_id>/note/<str:note_id>', views.getSpecificNote),
    path('note/<str:note_id>/delete', views.deleteNote),
    path('/health', views.health_check),
]

# 473c641c-276f-4761-9711-a19bfc9e3097