# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',


    url(
        regex=r'^miejscowosc-(?P<teryt_pk>\d+)/$',
        view=views.RegisterListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^$',
        view=views.RegisterListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^~create/$',
        view=views.RegisterCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^^miejscowosc-(?P<teryt_pk>\d+)/~create$',
        view=views.RegisterCreateView.as_view(),
        name='create'
    ),

    url(
        regex=r'^~map/$',
        view=views.RegisterMapView.as_view(),
        name='map'
    ),

    url(
        regex=r'^api/list/$',
        view=views.register_api,
        name='list_api'
    ),
    url(
        regex=r'^api/list/-(?P<teryt_pk>\d+)/$',
        view=views.register_api,
        name='list_api'
    ),
    url(
        regex=r'^api/detail/(?P<pk>\d+)$',
        view=views.register_api,
        name='list_api'
    ),

    url(
        regex=r'^(?P<slug>[\w-]+)/$',
        view=views.RegisterDetailView.as_view(),
        name='detail'
    ),
)
