import django
import os
import logging
import django.db.utils

log = logging.getLogger(__info__)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crabotter.settings.prod")

    django.setup()

    from django.contrib.auth.models import User

    try:
        User.objects.create_superuser(
            username=os.environ["SUPERUSER_USERNAME"],
            email=os.environ["SUPERUSER_EMAIL"],
            password=os.environ["SUPERUSER_PASSWORD"])
    except django.db.utils.IntegrityError:
        log.info("superuser already exists. Skipping createsuperuser.")