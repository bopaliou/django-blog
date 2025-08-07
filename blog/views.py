from django.shortcuts import render, get_object_or_404
from .models import Article


def home(request):
    articles = Article.objects.filter(est_publie=True).order_by('-date_publication')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, est_publie=True)
    return render(request, 'blog/article_detail.html', {'article': article})