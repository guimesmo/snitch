# coding: utf-8
import cyclone.escape
import cyclone.locale
from cyclone import web

from snitch.storage import DatabaseMixin
from snitch.utils import BaseLanguageHandler
from twisted.internet import reactor


class IndexHandler(BaseLanguageHandler):
    """
    Index page
    """
    @web.asynchronous
    def get(self):
        if self.current_user:
            self.redirect("/dashboard")
        else:
            self.render("index.html")
        reactor.callLater(2, self.do_something)

    def do_something(self):
        print "done!"


class LangHandler(BaseLanguageHandler):
    """
    Manager multiple language
    """
    def get(self, lang_code):
        if lang_code in cyclone.locale.get_supported_locales():
            self.set_secure_cookie("lang", lang_code)

        self.redirect(self.request.headers.get("Referer",
                                               self.get_argument("next", "/")))


class DashboardHandler(BaseLanguageHandler):
    @web.authenticated
    def get(self):
        self.render("dashboard.html")


class SampleSQLiteHandler(BaseLanguageHandler, DatabaseMixin):
    """
    Select sample
    """
    def get(self):
        if self.sqlite:
            response = self.sqlite.runQuery("select strftime('%Y-%m-%d')")
            self.write({"response": response})
        else:
            self.write("SQLite is disabled\r\n")
