from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from .models import Responses


def send_new_responses(responses_user, responses_text, responses_post):

    html_content = render_to_string(
        template_name='responses_email.html',
        context={
            'post_author': responses_post.author,
            'responses_user': responses_user,
            'text': responses_text,
            'link': f'{settings.SITE_URL}/detail/{responses_post.id}'
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новый отклик на ваше объявление!',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[responses_post.author.email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

#сигнал новый отклик
@receiver(post_save, sender=Responses)
def about_notify_new_replay(sender, instance, **kwargs):
    responses_user = instance.responses_user
    responses_text = instance.text
    responses_post = instance.post

    send_new_responses(responses_user, responses_text, responses_post)


