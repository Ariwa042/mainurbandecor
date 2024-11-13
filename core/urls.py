# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('contact/', views.ContactMessageView.as_view(), name='contact'),
    path('blog/', views.BlogPostListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_detail'),
    path('about/', views.about_view, name='about'),
]
