from django.contrib import admin
from .models import Task, Tile
# Register your models here.


class TaskInLine(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('launch_date', 'status',)
    list_display_links = ('launch_date',)
    list_filter = ('status',)
    list_editable = ('status',)
    actions = (admin.actions.delete_selected,)
    inlines = (TaskInLine,)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'type', 'tile',)
    list_display_links = ('title',)
    list_filter = ('type', 'tile',)
    list_editable = ('type', 'tile',)
    actions = (admin.actions.delete_selected,)
