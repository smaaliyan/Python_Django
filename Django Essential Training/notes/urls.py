from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes_list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='notes.details'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name= "notes.update"),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name= "notes.delete"),
    path('notes/new', views.NotesCreateView.as_view(), name= 'notes.new'), 
]