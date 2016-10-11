import logging
from django import forms
from .tasks import start_email


# Create your form here.


logger = logging.getLogger('custom')
logger.setLevel(logging.DEBUG)


class SearchForm(forms.Form):
    text = forms.CharField(label='Text', required=True)
    email = forms.EmailField(label='E-mail', required=True)

    def start(self):
        return start_email.apply_async(args=[self.data, ],
                                       soft_time_limit=0.0030)
