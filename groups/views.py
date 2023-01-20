from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView

from .models import Post, Comment, Group, Subscription
from .forms import PostForm, CommentForm, GroupForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class CommentListView(ListView):
    model = Comment
    template_name = 'post_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['pk'])


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'create_group.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GroupListView(ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'groups'


class GroupDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'
    context_object_name = 'group'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


@login_required
def subscribe_to_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    subscription = Subscription(subscriber=request.user, group=group)
    subscription.save()
    return redirect('group_detail', pk=group.pk)

@login_required
def unsubscribe_from_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    subscription = get_object_or_404(Subscription, subscriber=request.user, group=group)
    subscription.delete()
    return redirect('group_detail', pk=group.pk)


# def add_friend(request, pk):
#     friend = User.objects.get(pk=pk)
#     friend_request = Friend(user1=request.user, user2=friend, status='pending')
#     friend_request.save()
#     return redirect('friends')

# def confirm_friend_request(request, pk):
#     friend_request = get_object_or_404(Friend, pk=pk)
#     friend_request.status = 'accepted'
#     friend_request.save()
#     return redirect('friends')

# def remove_friend(request, pk):
#     friend = User.objects.get(pk=pk)
#     friend_request = get_object_or_404(Friend, user1=request.user, user2=friend)
#     friend_request.delete()
#     return redirect('friends')