from django.contrib import admin
from .models import SavedPassword

@admin.register(SavedPassword)
class SavedPasswordAdmin(admin.ModelAdmin):
    list_display = ('user', 'password', 'created_at')
