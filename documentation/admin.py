from django.contrib import admin
from .models import Documentation

@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["category", "title", "last_update_user", 'owner']}),
        ('Contenu', {'fields': ["banner", "content"]})
    ]

    exclude = ("created_at", "updated_at")

    list_display = ["category", "title", "owner", "last_update_user", "created_at", "updated_at"]
    list_filter = ["category", "title"]
    search_fields = ("category", "title", "content")
