from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model=Article
    template_name='home.html'



def ArticleDetailView(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    return render(request,'details.html',{"my":article})
"""   model =Article
    template_name=
    context_object_name = 'my'
   queryset = Article.objects.all()"""