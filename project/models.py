from django.db import models
from ckeditor.fields import RichTextField
from post.models import Tag

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = RichTextField()
    project_link = models.URLField()
    image = models.FileField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    tools = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    