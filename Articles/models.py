from django.db import models
from Users.models import User

class Article(models.Model):
    title=models.CharField(max_length=250, blank=False, null=False, verbose_name="Заголовок")
    text=models.TextField(blank=False, null=False, verbose_name="Текст статьи")
    created=models.DateTimeField(blank=False, null=False, auto_now_add=True, verbose_name="Опубликованно")
    changed=models.DateTimeField(blank=False, null=False, auto_now=True, verbose_name="Изменено")
    autor=models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank= False, verbose_name="Автор")
    onlysub=models.BooleanField(default=False, blank=False, null=False, verbose_name="Только для подписчиков")

    def __str__(self):
        return self.title
    class Meta:
        unique_together = ['title', 'autor']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
