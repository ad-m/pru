from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from braces.views import OrderableListMixin
from .models import Post, Tag

ORDER_FIELD = {'title': 'title'}


class PermissionMixin(object):

    def get_queryset(self, *args, **kwargs):
        qs = super(PermissionMixin, self).get_queryset(*args, **kwargs)
        return qs.for_user(self.request.user)


class PostDetailView(PermissionMixin, DetailView):
    model = Post


class PostListView(PermissionMixin, OrderableListMixin, ListView):
    model = Post
    paginate_by = 10
    orderable_columns = ("pk", "name", "city")
    orderable_columns_default = "created_on"

    def get_queryset(self, *args, **kwargs):
        qs = super(PostDetailView, self).get_queryset(*args, **kwargs)
        if 'tag_slug' in self.kwargs:
            self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            qs = qs.filter(tags__in=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        if hasattr(self, 'tag'):
            self.context['object'] = self.tag
        return context
