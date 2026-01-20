from celery import shared_task
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse
from .utils import trigger_swiftmassive_event
from .models import ApplicationReview

User = get_user_model()

def _send_event(self, email, event_name, payload):
    try:
        trigger_swiftmassive_event(
            email=email,
            event_name=event_name,
            data_dict=payload
        )
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

@shared_task(bind=True, max_retries=3)
def send_application_status_email(self, review_id):
    review = ApplicationReview.objects.select_related("application__applicant__user").get(pk=review_id)
    user = review.application.applicant.user
    _send_event(self, user.email, "application_status_update", {
        "first_name": user.first_name or user.username,
        "current_status": review.status,
        "login_url": f"{settings.SITE_URL}{reverse('dashboard')}"
    })

@shared_task(bind=True, max_retries=3)
def send_welcome_email_task(self, user_id):
    user = User.objects.get(pk=user_id)
    full_login_url = f"{settings.SITE_URL.rstrip('/')}{reverse('login')}"
    _send_event(self, user.email, "welcome_email", {
        "first_name": user.first_name or user.username,
        "login_url": full_login_url
    })

@shared_task(bind=True, max_retries=3)
def send_verification_email(self, user_email, token):
    _send_event(self, user_email, "verification_email", {"token": token})

@shared_task(bind=True, max_retries=3)
def send_status_update_email(self, user_email, status):
    _send_event(self, user_email, "status_update", {"status": status})
