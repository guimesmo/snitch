# coding: utf-8
import re
import hashlib
import cyclone.escape
from cyclone import web


class TemplateFields(dict):
    """Helper class to make sure our
        template doesn't fail due to an invalid key"""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self[name] = value


class BaseHandler(web.RequestHandler):
    """
    Render language files to template
    """
    _email = re.compile("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,8}$")

    def valid_email(self, email):
        return self._email.match(email)

    @staticmethod
    def encode_password(passwd):
        return hashlib.sha1(passwd).hexdigest()

    def get_user_locale(self):
        lang = self.get_secure_cookie("lang")
        if lang:
            return cyclone.locale.get(lang)
