from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Notes


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_details.html', {'details' : note})