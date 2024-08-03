from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Notes
from django.urls import reverse_lazy
from .forms import NotesForm
from django.views.generic.edit import DeleteView


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes_list')
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = reverse_lazy('notes_list')
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = reverse_lazy('notes_list')
    form_class = NotesForm


class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_details.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_details.html', {'details' : note})