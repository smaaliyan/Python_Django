from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Notes
from django.urls import reverse_lazy



class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = reverse_lazy('notes_list')

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'notes'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_details.html', {'details' : note})