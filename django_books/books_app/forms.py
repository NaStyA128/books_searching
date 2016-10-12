import logging
from django import forms
from .tasks import start_email
from django.utils.translation import ugettext_lazy as _


# Create your form here.


logger = logging.getLogger('custom')
logger.setLevel(logging.DEBUG)


class SearchForm(forms.Form):
    text = forms.CharField(label=_('Текст'), required=True)
    email = forms.EmailField(label=_('E-mail'), required=True)

    def start(self, lang):
        return start_email.apply_async(args=[self.data, lang],
                                       soft_time_limit=20)
