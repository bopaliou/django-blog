from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article


def home(request):
    articles_list = Article.objects.filter(est_publie=True).order_by('-date_publication')
    paginator = Paginator(articles_list,9)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, est_publie=True)
    return render(request, 'blog/article_detail.html', {'article': article})