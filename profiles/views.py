from django.http import HttpResponse
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Profiles with test key")
    if len(request.POST):
        for key, value in request.POST.items():
            logger.info(f"{key} = {value}")
    return HttpResponse("Profiles index view")
