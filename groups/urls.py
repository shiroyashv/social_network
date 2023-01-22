from django.urls import path

from .views import CommentCreateView, CommentListView, GroupCreateView, GroupDetailView, GroupListView, PostCreateView, PostDetailView, PostListView, dislike_post, like_post, subscribe_to_group, unsubscribe_from_group


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/', CommentListView.as_view(), name='post_comments'),
    path('post/<int:pk>/comment/create/', CommentCreateView.as_view(), name='create_comment'),
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('group/create/', GroupCreateView.as_view(), name='create_group'),
    path('group/<slug:slug>/', GroupDetailView.as_view(), name='group_detail'),
    path('post/<int:post_id>/like/', like_post, name='like'),
    path('post/<int:post_id>/dislike/', dislike_post, name='dislike'),
    path('post/<int:group_id>/subscribe/', subscribe_to_group, name='subscribe'),
    path('post/<int:group_id>/unsubscribe/', unsubscribe_from_group, name='unsubscribe'),
]
