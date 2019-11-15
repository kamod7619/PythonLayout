#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
Developed by Mr Kamod Kumar(Software Engineer)
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

