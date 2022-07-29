from django.http import HttpResponse
import logging

from posts.models import Post

logger = logging.getLogger(__name__)


def index(request):
    get_params = request.GET.items()
    post_list = Post.objects.all()
    for key, value in get_params:
        if key == 'title':
            post_list = post_list.filter(title__icontains=value)
        if key == 'slug':
            post_list = post_list.filter(slug__icontains=value)
        if key == 'created_at':
            post_list = post_list.filter(created_at__lt=value)
        if key == 'author_id':
            post_list = post_list.filter(autor_id=value)
    # post_list = post_list.filter(author=request.user)
    return HttpResponse(", ".join([x.title for x in post_list]))
