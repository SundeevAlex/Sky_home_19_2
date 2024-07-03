from django.db import models
from users.models import User

NULLABLE = {'blank': 'True', 'null': 'True'}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", help_text='Введите наименование продукта')
    description = models.TextField(verbose_name="Описание", help_text='Введите описание продукта', **NULLABLE)
    image = models.ImageField(upload_to="products/photo", help_text='Загрузите фото продукта', **NULLABLE)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена", help_text='Введите цену продукта', **NULLABLE)
    # manufactured_at = models.DateField(verbose_name="Дата создания", **NULLABLE)
    created_at = models.DateField(
        auto_created=True, verbose_name="Дата создания", **NULLABLE
    )
    updated_at = models.DateField(
        auto_now_add=True, verbose_name="Дата изменения", **NULLABLE
    )
    owner = models.ForeignKey(
        User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL
    )
    is_published = models.BooleanField(
        default=False, verbose_name='Опупликован'
    )

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']
        permissions = [
            ('can_edit_description', 'Can edit description'),
            ('can_edit_category', 'Can edit category'),
            ("can_change_is_published", "Can change is published of publication")
        ]


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", help_text='Введите наименование категории')
    description = models.TextField(verbose_name="Описание", help_text='Введите описание категории', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",)
    num_of_version = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    is_active_version = models.BooleanField(default=True, verbose_name='Теущая версия')

    def __str__(self):
        return f'{self.version_name} - {self.num_of_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
