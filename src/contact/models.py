from django.db import models
from django.utils.text import slugify
from text_unidecode import unidecode

class Contact(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='contact')
    description = models.TextField()
    location = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Contact, self).save(*args, **kwargs)


class Feedback(models.Model):
    fullname = models.CharField(max_length=40)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=13)
    message = models.TextField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname