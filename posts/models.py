from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='nome')
    description = models.TextField(blank=True, verbose_name='descrição')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='nome')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __str__(self):
        return self.name


def post_cover_path(instance, filename):
    return f'posts/{instance.author.username}/{filename}'


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Rascunho'
        IN_REVIEW = 'in_review', 'Em análise'
        PUBLISHED = 'published', 'Publicado'
        REJECTED = 'rejected', 'Rejeitado'

    title = models.CharField(max_length=200, verbose_name='título')
    content = models.TextField(verbose_name='conteúdo')
    cover_image = models.ImageField(
        upload_to=post_cover_path,
        blank=True,
        null=True,
        verbose_name='imagem de capa',
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='status',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='autor',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='categoria',
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='posts',
        verbose_name='tags',
    )
    views_count = models.PositiveIntegerField(default=0, verbose_name='visualizações')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='publicado em')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_published(self):
        return self.status == self.Status.PUBLISHED

    def can_be_edited(self):
        return self.status in (self.Status.DRAFT, self.Status.REJECTED)

    def can_be_sent_to_review(self):
        return self.status in (self.Status.DRAFT, self.Status.REJECTED)