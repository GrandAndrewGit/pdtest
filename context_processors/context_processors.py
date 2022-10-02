from django.conf import settings


def my_context_processor(request):
    return {'SOME_VAR': settings.TIME_ZONE}

