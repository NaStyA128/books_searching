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
    time = forms.FloatField(label=_('Время поиска'), min_value=0.5,
                            required=False)

    def start(self, lang):
        if self.data['time']:
            if start_email.apply_async(
                    args=[self.data, lang],
                    soft_time_limit=float(self.data['time'])):
                return self.data
        else:
            if start_email.apply_async(args=[self.data, lang]):
                return self.data
