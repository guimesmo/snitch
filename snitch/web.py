# coding: utf-8
import cyclone.locale
import cyclone.web

from snitch import views
from snitch import config
from snitch.storage import DatabaseMixin


class Application(cyclone.web.Application):
    def __init__(self, config_file):
        handlers = [
            (r"/",              views.IndexHandler),
            (r"/lang/(.+)",     views.LangHandler),
            # (r"/dashboard",     views.DashboardHandler),
            # (r"/account",       views.AccountHandler),
            # (r"/signup",        views.SignUpHandler),
            (r"/signin",        views.SignInHandler),
            # (r"/signout",       views.SignOutHandler),
            # (r"/passwd",        views.PasswdHandler),
            (r"/sample/sqlite", views.SampleSQLiteHandler),
        ]

        conf = config.parse_config(config_file)

        # Initialize locales
        if "locale_path" in conf:
            cyclone.locale.load_gettext_translations(conf["locale_path"],
                                                     "snitch")

        # Set up database connections
        # DatabaseMixin.setup(conf)
        DatabaseMixin.sync_db(conf)

        conf["login_url"] = "/signin"
        conf["autoescape"] = None
        cyclone.web.Application.__init__(self, handlers, **conf)
