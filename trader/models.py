from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Subscription(models.Model):
    email = models.EmailField(primary_key=True, max_length=64)
    is_active = models.BooleanField(default=True)


class Categories(models.Model):
    category = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.category}"

    def save(self, *args, **kwargs):
        if not Categories.objects.filter(category=self.category).exists():
            super(Categories, self).save(*args, **kwargs)
        else:
            raise ValidationError("Already Exists")


class Articles(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    source = models.URLField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ('-timestamp',)

    def serialize(self):
        return {
            "title": self.title,
            "body": self.body,
            "source": self.source,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "type": self.type.category,
        }

    def __str__(self):
        return f"{self.title} on {self.timestamp}"
