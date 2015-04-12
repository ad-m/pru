# from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin
from braces.views import UserFormKwargsMixin
from braces.views import FormValidMessageMixin
from braces.views import OrderableListMixin
from teryt.models import JednostkaAdministracyjna as Teryt
from .utils import paginator
from .utils import serializer_page
from .models import Register
from .forms import RegisterForm


ORDER_FIELD = {'title': 'title',
               'created': 'created',
               'voivodeship': 'community__parent__parent', }

API_FIELD = ('title', 'lat', 'lng', 'get_absolute_url', )


class PermissionMixin(object):

    def get_queryset(self, *args, **kwargs):
        qs = super(PermissionMixin, self).get_queryset(*args, **kwargs)
        return qs.for_user(self.request.user)


class RegisterCreateView(LoginRequiredMixin, UserFormKwargsMixin, FormValidMessageMixin,
         CreateView):
    model = Register
    form_class = RegisterForm

    def get_form_kwargs(self):
        kwargs = super(RegisterCreateView, self).get_form_kwargs()
        if 'teryt_pk' in self.kwargs:
            kwargs.update({'teryt': get_object_or_404(Teryt, pk=self.kwargs['teryt_pk'])})
        return kwargs

    def get_form_valid_message(self):
        return u"{0} created!".format(unicode(self.object))


class RegisterListView(PermissionMixin, OrderableListMixin, ListView):
    orderable_columns = ORDER_FIELD.values()
    orderable_columns_default = u"id"
    model = Register
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(RegisterListView, self).get_context_data(**kwargs)
        if hasattr(self, 'teryt'):
            context['teryt'] = self.teryt
            context['breadcrumbs'] = self.teryt.get_ancestors()
            context['children'] = self.teryt.get_children()
        else:
            context['children'] = Teryt.objects.filter(parent__isnull=True).all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(RegisterListView, self).get_queryset(*args, **kwargs)
        qs = qs.select_voivodeship()

        if 'teryt_pk' in self.kwargs:
            self.teryt = get_object_or_404(Teryt, pk=self.kwargs['teryt_pk'])
            qs = qs.community(self.teryt)
        return qs


class RegisterDetailView(PermissionMixin, DetailView):
    model = Register


class RegisterMapView(TemplateView):
    template_name = 'registers/register_map.html'


def register_api(request, pk=None, pk_teryt=None):
    object_list = Register.objects.public()

    if pk_teryt:
        object = get_object_or_404(Teryt, pk=pk)
        object_list = object_list.community(object)
    if pk:
        object_list = object_list.filter(pk=pk)
    paginated = paginator(request, object_list.all())
    results = serializer_page(paginated, API_FIELD)

    return JsonResponse(results, safe=False)
