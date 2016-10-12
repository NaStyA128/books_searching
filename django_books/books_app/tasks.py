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
            # result_pages.extend(get_list_or_404(
            #     Page, text__icontains=data.get('text', None))[:1])
            result_pages.extend(get_list_or_404(
                Page, text__icontains=data.get('text', None)))
            end_time = time()
            logger.info('Time select: {}'.format(end_time - start_time))
            if result_pages:
                logger.info('It generate message for send mail.')
                activate(lang)
                message = SimpleTemplateResponse(
                    'message.html', {'result_pages': result_pages})
                message.render()
                return send_email(text=message.content.decode('utf-8'),
                                  to=data.get('email', None))
            else:
                return False
        else:
            return False
    except SoftTimeLimitExceeded as softEx:
        logger.error('SoftTimeLimitExceeded: {}'.format(softEx.__dict__))
        # if result_pages:
        #     message = SimpleTemplateResponse(
        #         'message.html', {'result_pages': result_pages})
        #     message.render()
        #     return send_email(text=message.content.decode('utf-8'),
        #                       to=data.get('email', None))
        # else:
        #     return False


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
