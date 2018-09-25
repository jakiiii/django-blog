from django.urls import path

from . views import (
    PostListView,
    PostDetailsView,
    CreatePostFrom,
    PostUpdateView,
    ArchiveListView,
    PostDeleteView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('category/<int:pk>/', PostListView.as_view(), name='category'),
    path('create/', CreatePostFrom.as_view(), name='create-post'),
    path('archive/', ArchiveListView.as_view(), name='archive'),
    path('edit/<slug:slug>', PostUpdateView.as_view(), name='update'),
    path('blog/<slug:slug>/', PostDetailsView.as_view(), name='details'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='delete'),
]
