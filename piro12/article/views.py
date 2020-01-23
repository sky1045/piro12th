from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse
from django.http import HttpResponse
from article.models import Article, Comment


def list_article(request):
    articles = Article.objects.all()
    data = {
        'articles': articles
    }
    return render(request, 'list_article.html', data)


def detail_article(request, pk):
    article = Article.objects.get(pk=pk)
    data = {
        'article': article
    }
    return render(request, 'detail_article.html', data)


def create_article(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        if title and content:
            article = Article.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect(reverse('detail-article', kwargs={'pk': article.pk}))
    return render(request, 'create_article.html')


def create_comment(request, pk):
    article = Article.objects.get(pk=pk)
    content = request.POST.get('content', None)
    if content:
        comment = Comment.objects.create(
            article=article,
            content=content,
            author=request.user
        )
        return render_to_response('comment.html', {'comment': comment})
    else:
        return HttpResponse('댓글 내용을 입력해야 합니다.', 400)
    return redirect(reverse('detail-article', kwargs={'pk': article.pk}))
