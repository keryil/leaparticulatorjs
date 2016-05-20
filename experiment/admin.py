from django.contrib import admin
from .models import *
from django.conf import settings
# import bulk_admin
# from django import forms
# from glob import glob


def addMultipleMeanings(modeladmin, request, queryset):
    print "addMultipleMeanings reporting in"
addMultipleMeanings.short_description = "Batch add meanings"




class MeaningAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'url', 'preview')
    actions = ['addAllMeanings']
    # change_form_template = "admin/experiment/meaning/change_meaning_form.html"

    def addAllMeanings(self, request, queryset):
        """
        Adds all files in the /static/media/meanings
        directory as meanings.
        :param request:
        :param queryset:
        :return:
        """
        # if not self.has_add_permission():
        #     from django.core.exceptions import PermissionDenied
        #     raise PermissionDenied()

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
            except:
                pass

            # print "Helloooo", m
        self.message_user(request, "{} new meanings added.".format(
            counter))

    addAllMeanings.short_description = "Add all available files as meanings!"


admin.site.register(Meaning, MeaningAdmin)


class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('display_name',)
admin.site.register(Experiment, ExperimentAdmin)


class MeaningSpaceAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'preview')
admin.site.register(MeaningSpace, MeaningSpaceAdmin)


models = [Participant, Session, Round]
for m in models:
    admin.site.register(m)