from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.core.cache import cache
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import requests
import logging

from django.utils.decorators import method_decorator


logger = logging.getLogger(__name__)  # playground.views

# def say_hello(request):
#     # subject - message - from - list of recipients
#     # try:
#     #     send_mail('subject', 'message', 'info@daniel.com', ['bob@moshbuy.com'])
#     # except BadHeaderError:
#     #     pass

#     # try:
#     #     mail_admins('subject', 'message', html_message='message')
#     # except BadHeaderError:
#     #     pass

#     try:
#         # message = EmailMessage('subject', 'message',
#         #                        'from@daniel.com', ['danny@daniel.com'])
#         # message.attach_file('playground/static/images/dog.jpg')
#         # message.send()

#         message = BaseEmailMessage(
#             template_name='email/hello.html',
#             context={'name': 'Mosh'}
#         )
#         message.send(['danny@daniel.com'])
#     except BadHeaderError:
#         pass

#     return render(request, 'hello.html', {'name': 'Mosh'})


# def say_hello(request):
#     notify_customers.delay('Hello')
#     return render(request, 'hello.html', {'name': 'Mosh'})

class HelloView(APIView):
    # @method_decorator(cache_page(5*60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbins is offline')

        return render(request, 'hello.html', {'name': 'Mosh'})


# @cache_page(5*60)
# def say_hello(request):
#     key = 'httpbin_result'
#     # if cache.get(key) is None:
#     #     response = requests.get('https://httpbin.org/delay/2')
#     #     data = response.json()
#     #     # default cache = 5 mins
#     #     cache.set(key, data)
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': cache.get(key)})
