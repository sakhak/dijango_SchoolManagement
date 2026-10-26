from django.conf import settings


def site_context(request):
    """Global context available to every template."""
    return {
        'SITE_NAME': 'School Management System',
    }
