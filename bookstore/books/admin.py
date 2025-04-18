from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author')
    
    # Add filters to filter books by their attributes
    list_filter = ('author',)
    
    # Add search functionality to search by title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin interface
admin.site.register(Book, BookAdmin)
