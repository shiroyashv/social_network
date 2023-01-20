from django.urls import path

from .views import CommentCreateView, CommentListView, GroupCreateView, GroupDetailView, GroupListView, PostCreateView, PostDetailView, PostListView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/', CommentListView.as_view(), name='post_comments'),
    path('post/<int:pk>/comment/create/', CommentCreateView.as_view(), name='create_comment'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('group/create/', GroupCreateView.as_view(), name='create_group'),
    path('group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
]
