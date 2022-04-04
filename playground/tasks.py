
from email import message

from time import sleep
from celery import shared_task

# @celery.task # playground apps depends of storefront ==> no more independent app


@shared_task
def notify_customers(message):
    print('sending 10k emails...')
    print(message)
    sleep(10)
    print('emails were successfully sent!')
