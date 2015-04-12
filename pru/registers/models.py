from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from teryt.models import JednostkaAdministracyjna
from model_utils import Choices
# TODO: Manager - public(), area()


class Community(JednostkaAdministracyjna):

    def get_absolute_url(self):
        url = reverse('registers:list', kwargs={'teryt_pk': self.pk})
        print url
        return url

    def get_absolute_api(self):
        return reverse('registers:list_api', kwargs={'teryt_pk': self.pk})

    class Meta:
        proxy = True


class RegisterQuerySet(models.QuerySet):
    # Available on both Manager and QuerySet.
    def public(self):
        return self.filter(public=True)

    def community(self, community, itself=True):
        return self.filter(community__in=community.get_descendants(itself))

    def for_user(self, user):
        if user.has_perm('registers.change_register'):
            return self
        return self.filter(public=True)

    def select_voivodeship(self):
        return self.select_related('community__parent__parent')


class Register(models.Model):
    STATUS = Choices((0, 'yes', _('yes')),
                     (1, 'no', _('no')),
                     (2, 'unknown', _('unknown')))
    slug = AutoSlugField(unique=True, populate_from='title')
    img = models.ImageField(null=True, blank=True, verbose_name=_("Featured image"))
    title = models.CharField(max_length=150, verbose_name=_("Institution name"))

    contractor = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_("Contractor data"), help_text=_('Name of each contractor'))
    id_data = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_("ID data of contractor"),
        help_text=_("Machine readable of contractor eg. KRS, REGON"))
    value = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Value of contract'),
        help_text=_('Value of each contract are published'))
    privacy = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Individual person name'),
        help_text=_('Name of contractor, even individual person'))
    text = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Text format'),
        help_text=_('Datasheet are published as text'))
    comparable = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Comparable'),
        help_text=_('Data are published in comparable form eg. spreadsheet, not PDF'))
    scan = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Scan'),
        help_text=_('Scan of most contract without enquire'))
    spending = models.IntegerField(choices=STATUS, default=STATUS.unknown,
        verbose_name=_('Information about spending'),
        help_text=_('Published data contains information about spneding without contracts too'))

    comment = models.TextField(verbose_name=_("Comment"), blank=True,
        help_text=_('Extra information about registers eg. story of publishing, heroes'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Reporter"),
        help_text=_('User who report contracts to us'))
    community = models.ForeignKey(Community, limit_choices_to={'level': 2},
        verbose_name=_('Community'))
    lat = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Longtitude'))
    lng = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Langtitude'))
    url = models.URLField(verbose_name=_("URL of publication"))
    public = models.BooleanField(default=False, verbose_name=_("Public"),
        help_text=_("Mark to publish on site"))
    created = models.DateTimeField(editable=False, verbose_name=_("Creation date"),
        auto_now_add=True)
    modified = models.DateTimeField(editable=False, verbose_name=_("Last modification date"),
        help_text=_("Date of last modification of this object"), auto_now=True)
    objects = RegisterQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('registers:detail', kwargs={'slug': self.slug})

    def get_absolute_api(self):
        return reverse('registers:list_api', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title
