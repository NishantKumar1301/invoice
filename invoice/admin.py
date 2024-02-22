from django.contrib import admin
from .models import UploadedImage


@admin.register(UploadedImage)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'uploaded_at', 'question']
