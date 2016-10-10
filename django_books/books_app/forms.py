import logging
from django import forms
from django.core.mail import EmailMultiAlternatives
from smtplib import SMTPException
from .models import Page


# Create your form here.


FORMAT = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s ' \
         u'[%(asctime)s]  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO,
                    filename=u'logs_django.log')


class SearchForm(forms.Form):
    text = forms.CharField(label='Text', required=True)
    email = forms.EmailField(label='E-mail', required=True)

    # def start(self):
    #     data = self.data
    #     if data.get('text', None):
    #         result_pages = Page.objects.search_text(
    #             text=data.get('text', None)
    #         )
    #         logging.info('It form message for send mail.')
    #         str_message = '<div>'
    #         for page in result_pages:
    #             str_message += '<div style="margin-bottom: 10px; ' \
    #                            'border-bottom: 1px solid black">'
    #             str_message += '<p>Автор: {}</p>'.format(page.book.author)
    #             str_message += '<p>Книга: {}</p>'.format(page.book.name_book)
    #             str_message += '<p>Часть: {}</p>'.format(page.part)
    #             str_message += '<p>Раздел: {}</p>'.format(page.section)
    #             str_message += '<p>Глава: {}</p>'.format(page.chapter)
    #             str_message += '<p>Страница: {}</p>'.format(page.page_number)
    #             str_message += '</div>'
    #         str_message += '</div>'
    #         return self.send_email(text=str_message,
    #                                to=data.get('email', None))
    #     else:
    #         return False

    @staticmethod
    def send_email(text, to):
        try:
            email = EmailMultiAlternatives(
                'Results',
                text,
                to=[to]
            )
            email.attach_alternative(text, 'text/html')
            logging.info('It send the message to user {}'.format(to))
            return email.send()
        except SMTPException as ex:
            logging.exception(
                'Error send mail! SMTPException: {}'.format(ex.__dict__))
            return False
