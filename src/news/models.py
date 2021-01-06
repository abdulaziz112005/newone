from django.db import models
from django.utils.text import slugify
from text_unidecode import unidecode


class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Tags, self).save(*args, **kwargs)


class Articles(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, unique=True)
    description = models.CharField(max_length=1024)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news')
    views_count = models.IntegerField(default=0, blank=True, null=False)
    is_actual = models.BooleanField(default=False, null=False)
    is_columnist = models.BooleanField(default=False, null=False)
    is_dephoto = models.BooleanField(default=False, null=False)
    tags = models.ManyToManyField(Tags)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super(Articles, self).save(*args, **kwargs)

    @property
    def imageUrl(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


