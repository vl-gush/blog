from django.http import HttpResponse
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def profiles(request):
    message = []
    for key, value in request.GET.items():
        message.append(f'{key} = {value}')

    if len(request.POST):
        for key, value in request.POST.items():
            logger.info(f"{key} = {value}")

    if len(message):
        return HttpResponse(f"Profile view with GET params: {', '.join(message)}")
    return HttpResponse("Profile view")
