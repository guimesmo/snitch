from twisted.web.static import File
from twisted.web.resource import Resource

root_url = Resource()

# serve static files
root_url.putChild("static", File("/static"))
