from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView

from .forms import WordForm
from .models import Word


class WordListView(ListView):
    """Выводит список слов из БД."""
    model = Word
    template_name = 'words/word_list.html'


class WordCreateView(CreateView):
    """Добавляет слово в БД."""
    model = Word
    fields = ('word', 'translate')


def words_delete(request, pk):
    """Удаляет слово из БД."""
    get_object_or_404(Word, pk=pk).delete()
    return redirect('words:list')
