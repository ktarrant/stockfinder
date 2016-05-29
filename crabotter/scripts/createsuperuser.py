import django
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crabotter.settings.prod")

    django.setup()

    from django.contrib.auth.models import User

    User.objects.create_superuser(
        username=os.environ["SUPERUSER_USERNAME"],
        email=os.environ["SUPERUSER_EMAIL"],
        password=os.environ["SUPERUSER_PASSWORD"])