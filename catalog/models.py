from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", help_text='Введите наименование продукта')
    description = models.TextField(verbose_name="Описание", help_text='Введите описание продукта', **NULLABLE)
    image = models.ImageField(upload_to="media/photo", help_text='Загрузите фото продукта', **NULLABLE)
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

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование", help_text='Введите наименование категории')
    description = models.TextField(verbose_name="Описание", help_text='Введите описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
