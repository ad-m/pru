from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from autoslug import AutoSlugField
from registers.models import Register


class Tag(models.Model):
    slug = AutoSlugField(unique=True, populate_from='title')
    title = models.CharField(max_length=150, verbose_name=_("Tag name"))

    def get_absolute_url(self):
        return reverse('blog:list', kwargs={'tag_slug': self.slug})

    def __unicode__(self):
        return self.title


class PostQuerySet(models.QuerySet):
    def public(self):
        return self.filter(public=True)

    def for_user(self, user):
        if user.has_perm('blog.change_post'):
            return self
        return self.filter(public=True)


class Post(models.Model):
    slug = AutoSlugField(unique=True, populate_from='title')
    img = models.ImageField(null=True, blank=True, verbose_name=_("Featured image"))
    title = models.CharField(max_length=150, verbose_name=_("Post title"))
    registers = models.ManyToManyField(Register, null=True, blank=True)
    public = models.BooleanField(default=False, verbose_name=_("Public"),
        help_text=_("Mark to publish on site"))
    comment = models.TextField(verbose_name=_("Comment"), blank=True)
    created = models.DateTimeField(editable=False, verbose_name=_("Creation date"),
        auto_now_add=True)
    modified = models.DateTimeField(editable=False, verbose_name=_("Last modification date"),
        help_text=_("Date of last modification of this object"), auto_now=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title
