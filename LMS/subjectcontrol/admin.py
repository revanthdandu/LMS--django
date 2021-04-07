from django.contrib import admin
from .models import Notes, NotesFiles
from .models import Assignments, AssignmentsFiles

# admin.site.register(SubjectControl)
# admin.site.register(SubjectFiles)

class NotesFilesAdmin(admin.TabularInline):
    model = NotesFiles

class NotesAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    inlines = [NotesFilesAdmin]

admin.site.register(Notes, NotesAdmin)


class AssignmentsFilesAdmin(admin.TabularInline):
    model = AssignmentsFiles

class AssignmentsAdmin(admin.ModelAdmin):
    inlines = [AssignmentsFilesAdmin]

admin.site.register(Assignments, AssignmentsAdmin)