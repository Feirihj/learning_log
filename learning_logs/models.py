from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """Тема, которую изучает пользователь."""

    text = models.CharField("название", max_length=200)
    date_added = models.DateTimeField("дата создания", auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="владелец")

    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Запись по теме."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="тема")
    text = models.TextField("текст")
    date_added = models.DateTimeField("дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
