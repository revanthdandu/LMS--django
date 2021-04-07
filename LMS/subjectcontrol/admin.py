from django.contrib import admin
from .models import SubjectControl, SubjectFiles

# admin.site.register(SubjectControl)
# admin.site.register(SubjectFiles)

class SubjectFilesAdmin(admin.TabularInline):
    model = SubjectFiles

class SubjectControlAdmin(admin.ModelAdmin):
    # list_display = '__all__'
    inlines = [SubjectFilesAdmin,]

admin.site.register(SubjectControl, SubjectControlAdmin)