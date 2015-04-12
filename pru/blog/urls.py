# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=views.PostListView,
        name='list'
    ),
    url(
        regex=r'^tag-(?P<tag_slug>[\w-]+)/$',
        view=views.PostListView,
        name='list'
    ),

    url(
        regex=r'^(?P<slug>[\w-]+)/$',
        view=views.PostDetailView,
        name='detail'
    ),
)
