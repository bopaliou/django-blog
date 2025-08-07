from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_publication', 'est_publie')
    search_fields = ('titre', 'contenu')
    list_filter = ('est_publie', 'date_publication')
