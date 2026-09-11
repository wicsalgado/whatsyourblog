from django.conf import settings
from django.db import models

from posts.models import Post


class Comment(models.Model):
    content = models.TextField(verbose_name='conteúdo')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='autor',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='post',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author.username} em "{self.post.title}"'