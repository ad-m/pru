from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from braces.forms import UserKwargModelFormMixin
from .models import Register


class RegisterForm(UserKwargModelFormMixin, ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('registers:create')
        self.helper.layout = Layout(
            Fieldset(
                _('Office data'),
                'title',
                'community',
                'img',
            ),
            Fieldset(
                _('Data about ingredients of registers'),
                'id_data',
                'value',
                'privacy',
                'text',
                'comparable',
                'scan',
                'spending',
                'comment',
                'url',
            ),
            Submit('submit', _('Submit')),
        )

    def save(self, commit=False, *args, **kwargs):
        obj = super(RegisterForm, self).save(commit=False, *args, **kwargs)
        print self.user
        obj.user = self.user
        obj.save()
        return obj

    class Meta:
        model = Register
        fields = ('img', 'title', 'id_data', 'value', 'privacy', 'text', 'comparable', 'scan',
            'spending', 'comment', 'community', 'url')
