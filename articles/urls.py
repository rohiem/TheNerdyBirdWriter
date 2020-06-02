from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.ArticleListView.as_view(),name='home'),
    path('article/<int:article_id>',views.ArticleDetailView,name='articledetail')
]
