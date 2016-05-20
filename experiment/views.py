from django.shortcuts import render
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

from django.core.exceptions import PermissionDenied
from django.db import IntegrityError

from .models import Meaning
from easy_thumbnails.files import get_thumbnailer

# Create your views here.
def autodiscover_meanings(request):
    modeladmin = admin.site._registry[Meaning]
    if not modeladmin.has_add_permission(request):
        raise PermissionDenied()
    from glob import glob
    from os.path import join, basename

    files = glob(join(settings.MEDIA_ROOT,
                      "uploads", "meanings",
                      "*"))
    counter = 0
    for f in files:
        try:
            m = Meaning(display_name=basename(f),
                        image=f)
            m.save()
            counter += 1
        except IntegrityError:
            pass
    modeladmin.message_user(request, "{} new meanings added.".format(
        counter))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def thumbnail(request, meaning_id):
    try:
        meaning = Meaning.objects.get(id=meaning_id)
        thumbnail = meaning.thumbnail()
        return HttpResponse(thumbnail.read(), content_type="image/jpeg")
    except Meaning.DoesNotExist:
        pass