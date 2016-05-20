from __future__ import unicode_literals

from os.path import join

from django.db import models
from django.utils.html import format_html
from sortedm2m.fields import SortedManyToManyField
import easy_thumbnails

from Webiterated.settings import MEDIA_ROOT
from .fields import FileWithPreviewField
from .utils import filepath_to_static


# Metadata
class Experiment(models.Model):
    display_name = models.CharField(max_length=200)

    def __unicode__(self):
        return "Experiment '{}'".format(self.display_name)

# Experimental data

class Meaning(models.Model):
    display_name = models.CharField(max_length=200)
    image = FileWithPreviewField(path=join(MEDIA_ROOT, "uploads", "meanings"), unique=True)

    def preview(self):
        return format_html('<img src="{}"/>',
                           self.url())

    def thumbnail(self):
        from easy_thumbnails.files import get_thumbnailer
        thumbnailer = get_thumbnailer(self.image)
        options = {'size': (100, 100)}
        thumbnail = thumbnailer.get_thumbnail(options)
        return thumbnail

    def url(self):
        return filepath_to_static(self.image)
    url.admin_order_field = ('image')

    def __unicode__(self):
        return "{}({})".format(self.__class__.__name__, self.display_name)


class MeaningSpace(models.Model):
    display_name = models.CharField(max_length=200)
    meanings = SortedManyToManyField(Meaning)

    def preview(self):
        from django.contrib.staticfiles.templatetags.staticfiles import static
        from math import sqrt, ceil
        prevs = [filepath_to_static(p.thumbnail().url) for p in self.meanings.all()]
        rows = ceil(sqrt(len(prevs)))
        html = "<table><tr>"
        row_counter = 0
        for p in prevs:
            html += '<td align="center"><img src="{}"/></td>'
            row_counter += 1
            if row_counter % rows == 0:
                html += "</tr><tr>"
        # html +="</tr></table>"
        return format_html(html + "</tr></table>",
                           *prevs)

    def __unicode__(self):
        return "{}({})".format(self.__class__.__name__, self.display_name)

class Signal(models.Model):
    """
    Represents a signal created by participant
    """
    target = models.ForeignKey(Meaning)

class SignalData(models.Model):
    data_as_json = models.TextField()
    signal = models.ForeignKey(Signal)


class Participant(models.Model):
    display_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __unicode__(self):
        return "{}({})".format(self.__class__.__name__, self.display_name)


class Session(models.Model):
    experiment = models.ForeignKey(Experiment)
    display_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    started_at = models.DateTimeField(blank=True)
    ended_at = models.DateTimeField(blank=True)
    participants = SortedManyToManyField(Participant)
    # this is the largest possible meaning space
    meaning_space = SortedManyToManyField(MeaningSpace)

    def __unicode__(self):
        return "{}({})".format(self.__class__.__name__, self.display_name)

class Round(models.Model):
    """
    Represents an experimental round.
    """
    session = models.ForeignKey(Session)
    round_number = models.PositiveIntegerField()
    # this is the meaning space for the current round
    meaning_space = models.ForeignKey(MeaningSpace)
    signal = models.ForeignKey(Signal)
    speaker = models.ForeignKey(Participant, related_name="rounds_as_speaker")
    hearer = models.ForeignKey(Participant, related_name="rounds_as_hearer")
    target = models.ForeignKey(Meaning, related_name="rounds_as_target")
    guess = models.ForeignKey(Meaning, related_name="rounds_as_guess")
    options = SortedManyToManyField(Meaning, related_name="rounds_as_option")
    created_at = models.DateTimeField(auto_now_add=True)


