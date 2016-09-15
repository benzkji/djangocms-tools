# coding: utf-8
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, ugettext
from cms.models.pluginmodel import CMSPlugin

from cms_tools.models import CMSToolsPluginBaseModel


@python_2_unicode_compatible
class Gallery(CMSPlugin, CMSToolsPluginBaseModel):
    def __str__(self):
        return ugettext("Gallery")