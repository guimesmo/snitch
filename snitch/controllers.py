# coding: utf-8
import re
import hashlib
import uuid
from snitch.models import User
from snitch.storage import DatabaseMixin


class LoginController(DatabaseMixin):
    _email = re.compile("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,8}$")

    def validate_email(self, email):
        return self._email.match(email)

    @staticmethod
    def encode_password(passwd):
        salt = uuid.uuid4().hex
        return hashlib.sha512(passwd + salt).hexdigest()

    def set_password(self, email, password):
        password = self.encode_password(password)
        qs = self.sqlite.query(User).filter_by(email=email)
        if qs.exists():
            return qs.update(password=password)

    def create_user(self, email='', password='', nickname='', fullname=''):
        user = User()
        user.email = email
        user.password = self.encode_password(password)
        user.nickname = nickname
        user.fullname = fullname
        user.is_active = 1

        self.sqlite.add(user)
        self.sqlite.commit()

    def validate_user(self, email, password):
        print 'email ', email
        print 'password ', password
        print 'sqlite: ', dir(self.sqlite)
        print '-' * 80

        safe_password = self.encode_password(password)

        qs = self.sqlite.query(User).filter_by(email=email, password=safe_password)
        return qs.exists()
