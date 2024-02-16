from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Word(models.Model):
    """Модель для слов."""
    id = models.AutoField(
        primary_key=True
    )
    word = models.CharField(
        max_length=30,
        verbose_name='Слово',
        db_index=True,
        blank=False
    )
    translate = models.CharField(
        max_length=30,
        verbose_name='Перевод',
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        """Дополнительная информация о модели Word."""
        ordering = ('created_at',)
        unique_together = ('word', 'translate',)
        verbose_name = 'слово'
        verbose_name_plural = 'слова'

    def __str__(self):
        """Возвращает все поля подписки."""
        return (
            f'{self.word} — {self.translate}'
        )
