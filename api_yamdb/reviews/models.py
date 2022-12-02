from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from users.models import User


class Title(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    year = models.IntegerField(
        validators=[MaxValueValidator(timezone.now().year)], verbose_name='Год'
    )
    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        related_name='genre',
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='отзыв',
    )
    text = models.TextField(
        'Текст отзыва',
        help_text='Напишите нам отзыв об этом произведении',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    score = models.IntegerField(
        'оценка',
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]

    def __str__(self):
        return self.text[0:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Как вам отзыв?',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'комментарий: {self.text[0:15]}'


class GenreTitle(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    title = models.ForeignKey('Title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f'{self.name} {self.name}'
