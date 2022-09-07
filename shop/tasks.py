import time
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from accounts.models import Subscriber
from shop.models import Product

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active=True).values_list('email', flat=True)
    products = Product.objects.all()
    mail_text = render_to_string('email/email-subscribers.html', {
        'products': products
    })
    msg = EmailMultiAlternatives(subject='Product', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    msg.attach_alternative(mail_text, "text/html")
    msg.send()
