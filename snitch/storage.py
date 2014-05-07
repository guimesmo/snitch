# coding: utf-8
from twisted.python import log
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from snitch.models import Base


class DatabaseMixin(object):
    sqlite = None

    @classmethod
    def setup(cls, conf):
        if "sqlite_settings" in conf:
            try:
                # Default connection from cyclone
                # import cyclone.sqlite
                # DatabaseMixin.sqlite = \
                #     cyclone.sqlite.InlineSQLite(conf["sqlite_settings"].database)

                # Connection with sqlialchemy
                cls.engine = create_engine('sqlite:///%s' % conf["sqlite_settings"].database,
                                           echo=True)

                DBSession = sessionmaker(bind=cls.engine)
                cls.sqlite = DBSession()

            except Exception as sqlite_err:
                log.err("SQLite is currently disabled: %s" % sqlite_err)

    @classmethod
    def sync_db(cls, conf):
        cls.setup(conf)
        Base.metadata.bind = cls.engine
        Base.metadata.create_all(cls.engine)


    def __del__(self):
        try:
            self.sqlite.close()
        except:
            pass
