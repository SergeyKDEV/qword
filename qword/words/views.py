from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView

from .forms import WordForm
from .models import Word


class WordListView(ListView):
    """Выводит список слов из БД."""
    model = Word
    template_name = 'words/word_list.html'



class AddWord(CreateView):
    """Добавляет слово в БД."""
    template_name = 'words/word_add.html'
    form_class = WordForm

    def get_context_data(self, **kwargs):
        # TODO
        return  {
            'form': form
        }

    def form_valid(self, form):
        form.save()

    def get_success_url(self):
        return reverse('words:list')


def words_delete(request, pk):
    """Удаляет слово из БД."""
    get_object_or_404(Word, pk=pk).delete()
    return redirect('words:list')
