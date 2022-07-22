from django.conf import settings
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'MY_VAR = {settings.MY_VAR}')
    if settings.FIRST_VAR == '2':
        logger.info(settings.SECOND_VAR)
    elif settings.FIRST_VAR == '3':
        logger.info(settings.THIRD_VAR)
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Posts index view")
