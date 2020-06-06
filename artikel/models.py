from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class ArtikelModel(models.Model):
    judul = models.CharField(max_length=100)
    kategori = models.CharField(max_length=100)
    body = models.TextField()
    penulis = models.CharField(max_length=100)
    published = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.CharField(max_length=255, blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def get_absolute_url(self):
        return reverse('artikel:artikeldetail', kwargs={'slug': self.slug})

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)