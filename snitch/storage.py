import cyclone.sqlite
from twisted.python import log


class DatabaseMixin(object):
    sqlite = None

    @classmethod
    def setup(cls, conf):
        if "sqlite_settings" in conf:
            try:
                DatabaseMixin.sqlite = \
                cyclone.sqlite.InlineSQLite(conf["sqlite_settings"].database)
            except Exception as sqlite_err:
                log.err("SQLite is currently disabled: %s" % sqlite_err)
