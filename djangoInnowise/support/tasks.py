import datetime
from django.core.mail import send_mail
from djangoInnowise.celery import app
from celery import shared_task
from django.conf import settings
from .models import User, Ticket



@app.task
def support_answer():
    list_message = []
    for ticket in Ticket.objects.all():
        if ticket.id not in list_message:
            list_message.append(ticket.id)
            for user in User.objects.all():
                if user.id == ticket.user_id:
                    send_mail(
                        'Service support',
                        'some support answer',
                        settings.EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                    )

