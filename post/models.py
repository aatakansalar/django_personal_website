from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("post:tagposts", kwargs={'slug': self.slug})

class Post(models.Model):
    post_author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_content = RichTextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_image = models.FileField(blank=True, null=True, verbose_name="Resim Ekle:")
    post_tags = models.ManyToManyField(Tag, verbose_name="Add Tag", blank=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering =['-post_date']

    def get_post_tag(self, i):
        return self.post_tags.all()[i]

    def get_absolute_url(self):
        return reverse("post:post", kwargs={'slug': self.slug})
    

