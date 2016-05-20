from django import forms
from django.conf import settings
from django.utils.html import mark_safe
from django.template import Engine, Context
from django.template.loader import get_template
# from os.path import join
from experiment.utils import filepath_to_static


class FilePathFieldBrowser(forms.Select):

    def __init__(self, *args, **kwargs):
        super(FilePathFieldBrowser, self).__init__(*args, **kwargs)
        # self.allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        html = super(FilePathFieldBrowser, self).render(name=name,
                                                        value=value,
                                                        attrs=attrs,
                                                        choices=choices)
        # for c in self.choices:
        #     c.url = c[0]
        context = {'options': zip(self.choices,
                                  [filepath_to_static(c[0]) for c in self.choices])}
        # html = re.sub("option value='(.+?)'","option value=\1 style=\"background-image:url(\1)\"", html)
        # print html.replace("option", "option style="background-image:url(male.png);"")
        html += get_template("FilePathFieldBrowser.html").render(context) #""<img src='{}'></img>".format(choices[0])
        return mark_safe(html)

from django import forms
from django.conf import settings
from django.utils.html import mark_safe
from django.template import Engine, Context
from django.template.loader import get_template
# from os.path import join

class FilePathMultiFieldBrowser(forms.SelectMultiple):

    def __init__(self, *args, **kwargs):
        super(FilePathFieldBrowser, self).__init__(*args, **kwargs)
        # self.allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        html = super(FilePathFieldBrowser, self).render(name=name,
                                                        value=value,
                                                        attrs=attrs,
                                                        choices=choices)
        # for c in self.choices:
        #     c.url = c[0]
        urls = [settings.MEDIA_URL + "/" + "/".join(c[0].split("/")[-3:]) for c in self.choices]
        context = {'options': zip(self.choices,
                                  urls)}
        # html = re.sub("option value='(.+?)'","option value=\1 style=\"background-image:url(\1)\"", html)
        # print html.replace("option", "option style="background-image:url(male.png);"")
        html += get_template("FilePathFieldBrowser.html").render(context) #""<img src='{}'></img>".format(choices[0])
        return mark_safe(html)