# Copyright (C) 2015 AG Projects. See LICENSE for details.
#

import os
import sys

from application.python.descriptor import classproperty


class Resources(object):
    """Provide access to SylkServer's resources"""

    _cached_directory = None

    @classproperty
    def directory(cls):
        if cls._cached_directory is None:
            script = sys.argv[0]
            binary_directory = os.path.dirname(os.path.realpath(script))
            if os.path.basename(binary_directory) == 'bin':
                application_directory = os.path.dirname(binary_directory)
                resources_component = 'share/sylkserver'
            else:
                application_directory = binary_directory
                resources_component = 'resources'
            cls._cached_directory = os.path.join(application_directory, resources_component).decode(sys.getfilesystemencoding())
        return cls._cached_directory

    @classmethod
    def get(cls, resource):
        return os.path.join(cls.directory, resource or u'')

