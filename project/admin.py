from django.contrib import admin
from project.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_display_links = ['title', 'date']

    class Meta:
        model = Project