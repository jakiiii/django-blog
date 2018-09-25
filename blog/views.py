from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category, CoverImage
from .forms import CreatePostForm


class PostListView(ListView):
    model = Post
    context_object_name = 'posts_list'
    paginate_by = 6
    template_name = 'pages/home.html'

    def get_queryset(self):
        result = super(PostListView, self).get_queryset()
        query = self.request.GET.get('q')
        pk = self.kwargs.get('pk')
        if query:
            result = result.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        elif pk:
            result = Post.objects.filter(
                Q(category__exact=pk)
            )
        else:
            result = Post.objects.all()
        return result

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['category_list'] = Category.objects.all()
        context['cover_list'] = CoverImage.objects.all()
        context['title'] = 'Home'
        return context


class PostDetailsView(DetailView):
    model = Post
    template_name = 'pages/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailsView, self).get_context_data(*args, **kwargs)
        # context['related_post'] = Post.objects.filter(category=F('category'))[:3]
        context['category_list'] = Category.objects.all()
        context['cover_list'] = CoverImage.objects.all()
        context['title'] = '{}'.format(self.get_object().title)
        return context


class CreatePostFrom(LoginRequiredMixin, CreateView):
    form_class = CreatePostForm
    template_name = 'pages/from.html'
    login_url = '/accounts/'
    success_url = '/archive/'

    def get(self, request):
        obj = render(request, self.template_name, {"post": self.form_class})
        return obj

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.owner = self.request.user
        return super(CreatePostFrom, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(CreatePostFrom, self).get_context_data(*args, **kwargs)
        context['title'] = 'Create Post'
        return context


class ArchiveListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 5
    login_url = '/accounts/'
    context_object_name = 'archive_list'
    template_name = 'profiles/archive.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArchiveListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Archive'
        return context

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CreatePostForm
    template_name = 'pages/from.html'
    login_url = '/accounts/'
    success_url = '/archive/'

    def get(self, request, slug):
        return render(request, self.template_name, {"post": self.form_class})

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update: {}'.format(self.get_object().title)
        return context

    def form_valid(self, form):
        instance = form.save(commit=True)
        instance.owner = self.request.user
        return super(PostUpdateView, self).form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '/accounts/'
    template_name = 'pages/delete_confirmation.html'
    success_url = reverse_lazy('archive')

    def get_context_data(self, *args, **kwargs):
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Delete- {}'.format(self.get_object().title)
        return context
