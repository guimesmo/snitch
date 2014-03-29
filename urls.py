from twisted.web.static import File
from twisted.web.resource import Resource

root_url = Resource()

root_url.putChild("foo", File("/tmp"))
root_url.putChild("bar", File("/lost+found"))
root_url.putChild("baz", File("/opt"))
