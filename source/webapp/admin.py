from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'execute_at']
    list_filter = ['id', 'description', 'status', 'execute_at']
    search_fields = ['id', 'description']
    fields = ['description', 'status', 'execute_at']
    readonly_fields = ['id', 'execute_at']


admin.site.register(Task, TaskAdmin)

