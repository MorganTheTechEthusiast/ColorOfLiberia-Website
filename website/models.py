from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = f"{self.parent.name}-{self.name}" if self.parent else self.name
            self.slug = slugify(base)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parent.name} > {self.name}" if self.parent else self.name


class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='businesses')
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Liberia')  # or your target country
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class BusinessHour(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='hours')
    day = models.CharField(max_length=10)  # e.g. Monday
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.business.name} - {self.day}"


class BusinessMedia(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='media')
    logo = models.ImageField(upload_to='business_media/logo', blank=True, null=True)
    cover = models.ImageField(upload_to='business_media/cover', blank=True, null=True)
    image = models.ImageField(upload_to='business_media/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.business.name} Media"


class Review(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.business.name}"


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='bookmarked_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'business')

    def __str__(self):
        return f"{self.user.username} bookmarked {self.business.name}"
