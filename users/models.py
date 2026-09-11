from django.conf import settings
from django.db import models

from posts.models import Category, Tag


def profile_picture_path(instance, filename):
    return f'profiles/{instance.user.username}/{filename}'


class Profile(models.Model):
    MAX_TAGS = 3

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='usuário',
    )
    display_name = models.CharField(max_length=100, verbose_name='nome de exibição')
    bio = models.TextField(blank=True, verbose_name='biografia')
    profile_picture = models.ImageField(
        upload_to=profile_picture_path,
        blank=True,
        null=True,
        verbose_name='foto de perfil',
    )
    main_category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profiles',
        verbose_name='tema principal',
    )
    profile_tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='profiles',
        verbose_name='tags do perfil',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    def __str__(self):
        return self.display_name or self.user.username

    def has_reached_tag_limit(self):
        return self.profile_tags.count() >= self.MAX_TAGS