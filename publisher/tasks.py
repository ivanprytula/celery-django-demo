from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template import Template, Context

from publisher.models import Post
from quick_publisher.celery import celery_app

REPORT_TEMPLATE = """
    Here's how you did till now:
    
    {% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |
        
    {% endfor %}
"""


@celery_app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue

        template = Template(REPORT_TEMPLATE)

        send_mail(
            'Your QuickPublisher Activity',
            template.render(context=Context({'posts': posts})),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )
