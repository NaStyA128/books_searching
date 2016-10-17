import logging
import time
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
            # result = start_email.apply_async(
            #     args=[self.data, lang],
            #     soft_time_limit=float(self.data['time']))
            result = start_email.s(self.data, lang).apply_async(
                soft_time_limit=float(self.data['time']))
            # print(result.get(propagate=False))
            # print(result.ready())
            # self.bla(result)
            if result:
                return self.data
        else:
            result = start_email.s(self.data, lang)
            if result():
                return self.data

    @staticmethod
    def bla(result):
        while True:
            if result:
                if result.backend.get_result(result.id):
                    print('Result: {}'.format(
                        result.backend.get_status(result.id)))
                    break
                else:
                    print('No results: {}'.format(
                        result.backend.get_status(result.id)))
                    time.sleep(0.5)
            else:
                break
