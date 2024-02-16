from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import WordForm
from .models import Word


class WordListView(ListView):
    """Выводит список слов из БД."""
    model = Word
    template_name = 'words/word_list.html'


def words_add(request):
    """Добавляет слово в БД."""
    template_name = 'words/word_add.html'
    form = WordForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('words:list')
    return render(request, template_name, context)


def words_delete(request, pk):
    """Удаляет слово из БД."""
    get_object_or_404(Word, pk=pk).delete()
    return redirect('words:list')
