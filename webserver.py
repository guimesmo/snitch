from twisted.web.server import Site
from twisted.internet import reactor

from urls import root_url
import settings

factory = Site(root_url)
reactor.listenTCP(settings.DEFAULT_PORT, factory)
reactor.run()
