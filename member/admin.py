from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ["user", "country", "profile_picture", "current_species"]})
    ]
    list_display = ("user", "country")
    list_filter = ('country',)
