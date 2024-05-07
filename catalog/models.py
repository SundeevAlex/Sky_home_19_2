from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class Product(models.Model):
    pass

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']


class Category(models.Model):
    pass

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
