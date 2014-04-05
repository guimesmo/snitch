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
            qs = self.sqlite.execute("select * from users")
            rows = []
            for row in qs.fetchall():
                rows.append([i for i in row])

            self.write({'response': rows})
        else:
            self.write("SQLite is disabled\r\n")
