# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys


HELPER_SETTINGS = {
    'SITE_ID': 1,
    'TIME_ZONE': 'Europe/Zurich',
    'LANGUAGES': (
        ('en', 'English'),
        ('de', 'German'),
        ('fr', 'French'),
    ),
    'INSTALLED_APPS': [
        'parler',
        'treebeard',
        'aldryn_categories',
    ],
    'PARLER_LANGUAGES': {
        1: (
            {'code': 'de', },
            {'code': 'en', },
            {'code': 'fr', },
        ),
        'default': {
            # Do not remove or change this value or tests may break.
            'hide_untranslated': True,
            # Do not remove or change this value or tests may break.
            'fallback': 'fr',
        }
    },
    'CMS_CONFIRM_VERSION4': True,
}


def run():
    from djangocms_helper import runner
    extra_args = sys.argv[1:] if len(sys.argv) > 1 else []
    runner.cms('aldryn_categories', [sys.argv[0]], extra_args=extra_args)


if __name__ == "__main__":
    run()
