# -*- coding: utf-8 -*-
from django.test import TestCase, Client, modify_settings

# compat
import django
if django.VERSION[:2] < (1, 10):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


@modify_settings(INSTALLED_APPS={
    'append': 'djangocms_misc.autopublisher',
})
class AutoPublisherTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    # TODO: many autopublisher tests
    def test_save_page(self):
        pass

    def test_save_plugin(self):
        pass

    def test_move_plugin(self):
        pass

    def test_move_page(self):
        pass

    def test_save_static_placeholder_plugin(self):
        pass

    def test_move_static_placeholder_plugin(self):
        pass
