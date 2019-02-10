import logging
import pkg_resources

logger = logging.getLogger(__name__)

class Extension(object):
    name = None

def load_extensions():
    installed_extensions = []

    for entry_point in pkg_resources.iter_entry_points('rpicarserver.ext'):
        extension_class = entry_point.load(require=False)
        extension = extension_class()
        installed_extensions.append(extension_class())
        logger.debug('Loaded extension: %s', extension.name)

    return installed_extensions
