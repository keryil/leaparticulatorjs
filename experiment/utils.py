from django.conf import settings
# from os.path import join, sep


def filepath_to_static(f):
    print "URL", settings.MEDIA_URL
    print "ROOT", settings.MEDIA_ROOT
    print f
    print "Result", settings.MEDIA_URL + "/" + \
                f.replace(settings.MEDIA_ROOT,'')
    return settings.MEDIA_URL + "/" + \
                f.replace(settings.MEDIA_ROOT,'')