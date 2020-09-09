from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    post_author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    post_title = models.CharField(max_length=50)
    post_content = RichTextField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_image = models.FileField(blank=True, null=True, verbose_name="Resim Ekle:")
    def __str__(self):
        return self.post_title
    class Meta:
        ordering =['-post_date']
