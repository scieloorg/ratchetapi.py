import pkg_resources
import logging

# Setting up a do-nothing handler. We expect the application to define
# the handler for `ratchetapi`.
logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = pkg_resources.get_distribution('ratchetapi').version
__user_agent__ = 'ratchetapi/%s' % __version__

from .core import Connector, Endpoint, Client
