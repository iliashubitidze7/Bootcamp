from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celery.exceptions import SoftTimeLimitExceeded

@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def send_welcome_email(self,user_id):
    User = get_user_model()
    
    try:
        user = User.objects.get(id=user_id)

        subject = "Welcome to our Platform"
        message = f"Hi {user.first_name},\n\nWelcome to our platform!"
        from_email = "ilia.shubitidze@ge.anadoluefes.com"
        recipient_list = [user.email]


        send_mail(subject, message, from_email, recipient_list)

        print(f"Welcome email sent to {user.email}")
        return f"Email sent to {user.email}"
    
    except User.DoesNotExist:
         print(f"User with ID {user_id} does not exist.")
         return f"User not found"
    
    except Exception as exc:
        print(f"Error occurred: {exc}. Retrying...")
        raise self.retry(exc=exc)
    
    except SoftTimeLimitExceeded as exc:
        print(f"Time limit exceeded: {exc}. Retrying...")
        raise self.retry(exc=exc)




