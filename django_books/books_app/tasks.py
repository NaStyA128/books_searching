from __future__ import absolute_import
import logging
from django.core.mail import EmailMultiAlternatives
from django.template.response import SimpleTemplateResponse
from django.shortcuts import get_list_or_404
from django.utils.translation import activate
from django.utils.translation import ugettext as _
from smtplib import SMTPException
from .models import Page
from celery import shared_task
from celery.exceptions import SoftTimeLimitExceeded
from time import time


logger = logging.getLogger('custom')
logger.setLevel(logging.DEBUG)


@shared_task
def start_email(data, lang):
    result_pages = []
    try:
        if data.get('text', None):
            start_time = time()
            end_time = None
            i = 0
            while True:
                small_result = get_list_or_404(
                    Page, text__icontains=data.get('text', None))[i:i+5]
                i += 1
                if small_result:
                    result_pages.extend(small_result)
                    global end_time
                    end_time = time()
                    print(end_time - start_time)
                else:
                    break
            logger.info('Time select: {}'.format(end_time - start_time))
            return letter_formation(result_pages, lang, data.get(
                'email', None))
        else:
            return False
    except SoftTimeLimitExceeded as softEx:
        logger.error('SoftTimeLimitExceeded: {}'.format(softEx.__dict__))
        return letter_formation(result_pages, lang, data.get('email', None))


def send_email(text, to):
    try:
        email = EmailMultiAlternatives(
            _('Результаты'),
            text,
            to=[to]
        )
        email.attach_alternative(text, 'text/html')
        email.content_subtype = 'html'
        logger.info('It send the message to user {}'.format(to))
        return email.send()
    except SMTPException as ex:
        logger.exception(
            'Error send mail! SMTPException: {}'.format(ex.__dict__))
        return False


def letter_formation(results, lang, to):
    if results:
        logger.info('It generate message for send mail.')
        activate(lang)
        message = SimpleTemplateResponse(
            'message.html', {'result_pages': results})
        message.render()
        return send_email(text=message.content.decode('utf-8'),
                          to=to)
    else:
        return False
