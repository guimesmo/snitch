# coding: utf-8
import cyclone.escape
import cyclone.locale
from cyclone import web

from snitch.storage import DatabaseMixin
from snitch.controllers import LoginController
from snitch.utils import BaseHandler, TemplateFields
from twisted.internet import reactor
from twisted.internet import defer


class SignInHandler(BaseHandler, LoginController):
    """
    Register a new user
    """
    def get(self):
        if self.get_current_user():
            self.redirect("/")
        else:
            self.render("signin.html", fields=TemplateFields())

    @defer.inlineCallbacks
    def post(self):
        email = self.get_argument("email", "")
        passwd = self.get_argument("passwd", "")
        remember = self.get_argument("remember", "")

        f = TemplateFields(email=email, remember=remember)

        if not email:
            f["err"] = ["auth"]
            self.render("signin.html", fields=f)
            defer.returnValue(None)

        if not self.validate_email(email):
            f["err"] = ["auth"]
            self.render("signin.html", fields=f)
            defer.returnValue(None)

        if not passwd:
            f["err"] = ["auth"]
            self.render("signin.html", fields=f)
            defer.returnValue(None)

        if not self.validate_user(email, passwd):
            f["err"] = ["auth"]
            self.render("signin.html", fields=f)
            defer.returnValue(None)

        # set session cookie
        self.set_current_user(email=email,
                              expires_days=15 if remember else None)

        self.redirect("/")


class IndexHandler(BaseHandler):
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


class LangHandler(BaseHandler):
    """
    Manager multiple language
    """
    def get(self, lang_code):
        if lang_code in cyclone.locale.get_supported_locales():
            self.set_secure_cookie("lang", lang_code)

        self.redirect(self.request.headers.get("Referer",
                                               self.get_argument("next", "/")))


class DashboardHandler(BaseHandler):
    @web.authenticated
    def get(self):
        self.render("dashboard.html")


class SampleSQLiteHandler(BaseHandler, DatabaseMixin):
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
